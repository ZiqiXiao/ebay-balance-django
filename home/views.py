import os
import pytz
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import CheckingHistory
from django.core import serializers

import requests
from datetime import datetime

# Create your views here.


def index(request):
    # Page from the theme
    return render(request, 'includes/dashboard.html')


class EbayBalanceView(View):
    def get(self, request):
        history = CheckingHistory.objects.only(
            'gift_card_no', 'balance', 'time')
        history_json = serializers.serialize('json', history)
        context = {
            'history': history_json,
        }
        return render(request, 'includes/ebay_balance.html', context)

    def post(self, request):
        # 1. 解析POST请求
        gift_card_no = request.POST.get('giftCardNo')

        # 2. 将数据发送给另一个容器中的服务
        fastapi_banckend_host = os.environ.get('FASTAPI_BACKEND_HOST', 'http://172.17.0.3')
        response = requests.get(f'{fastapi_banckend_host}:8111/check-balance', params={
            'gift_card_no': gift_card_no
        })
        
        # 只有当响应状态码为200时，我们才考虑解析和保存数据
        if response.status_code == 200:
            data = response.json()
            
            # 3. 保存查询到的结果
            CheckingHistory.objects.create(
                gift_card_no=gift_card_no,
                balance=data['balance'],
                time=datetime.now(pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')
            )
            return HttpResponse('success')

        elif response.status_code == 503:
            return HttpResponse('当前没有可用端口，请等一下~', status=503)
        
        else:
            return HttpResponse('其他内部错误！', status=500)
        
