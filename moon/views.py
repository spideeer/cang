from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
from . import models



def homepage(requests):
    if requests.method=="POST":
        email = requests.POST.get('email','')  #1005302528@qq.com
        password = requests.POST.get('password','')
        try:
            user = models.UserInfo.objects.get(user_name=email,password=password)
        except Exception as f :
            return HttpResponse("<a>用户名或密码错误，请重新输入</a>")
        # print(user.id)
        # print(user.user_name)
        cargo_list = models.CargoInfo.objects.filter(userinfo_id=user)
        # for cargo in cargo_list:
        #     print(cargo.amount)
        # cargo = models.CargoInfo.objects.get(id=1)
        # print(cargo, '11111111111')
        # print(user)
        return render(requests,'smt.html',locals())

def create_new(requests):
    return HttpResponse("OK")

def peisional(requests):
    return HttpResponse("1")