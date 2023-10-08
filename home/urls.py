from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # ebay-balance
    path('', views.EbayBalanceView.as_view(), name='ebay_balance'),
]
