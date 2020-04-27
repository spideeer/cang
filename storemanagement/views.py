# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    if request.method=='GET':
        return render(request,'index.html')



#         remember=requests.POST.get('remember','')
#         username=requests.POST.get('username','')
#         password=requests.POST.get('password','')
#         #验证用户名密码
#         try:
#             user=models.User.objects.get(name=username,
#                                          password=password)
#             # requests.session['userinfo']={
#             #     "username":user.name,
#             #     'id':user.id
#             # }
#         except:
#             return HttpResponse('登录失败')
#
#         resp = HttpResponse('登陆成功')
#         if remember:
#             resp.set_cookie('username',username,7*24*60*60)
#         else:
#             resp.delete_cookie('username')
#         return resp