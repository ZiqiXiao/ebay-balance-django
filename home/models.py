from django.db import models
from django.utils import timezone

# Create your models here.


class CheckingHistory(models.Model):
    gift_card_no = models.CharField(max_length=13)
    balance = models.CharField(max_length=10)
    time = models.DateTimeField(default=timezone.now)
