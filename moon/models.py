
from django.db import models

class UserInfo(models.Model):

    user_name = models.CharField(max_length=100,)
    password = models.CharField(max_length=50)
class CargoInfo(models.Model):

    cargo_ID = models.CharField(max_length=30)
    cargo_name = models.CharField(max_length=100)
    amount = models.IntegerField(max_length=10)
    in_price = models.IntegerField(max_length=10)
    out_price = models.IntegerField(max_length=10)
    userinfo = models.ForeignKey(UserInfo)
#python manage.py makemigrations
#python manage.py migrate
# models.CargoInfo.objects.create(cargo_ID=8822,cargo_name="导弹",amount=100,in_price=100,out_price=330,userinfo=a[0])
# models.CargoInfo.objects.create(cargo_ID=8482,cargo_name="航母",amount=100,in_price=20,out_price=3600,userinfo=a[0])
# models.CargoInfo.objects.create(cargo_ID=3882,cargo_name="飞机",amount=100,in_price=240,out_price=340,userinfo=a[0])