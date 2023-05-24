from django.shortcuts import render
from django.http import HttpResponse
from bbs.models import *
# Create your views here.
def post(request):
    context={}
    context['title']=Post.objects.get(id=1).title
    context['body']=Post.objects.get(id=1).body
    return render(request,"post.html",context)

def posts(request):
    context={}
    context['posts']=Post.objects.all()
    return render(request,"posts.html",context)

def login(request):
    if request.method=='POST' and request.POST:
        if request.POST['action']=='login':
            now_user_name=request.POST['login-username']
            now_password=request.POST['login-password']
            try:
                user=User.objects.filter(user_name=now_user_name).get()
                if user.password==now_password:
                    return HttpResponse("登录成功！")
                else:
                    return HttpResponse("密码错误！")
            except:
                return HttpResponse("用户名不存在！")
        elif request.POST['action']=='register':
            now_user_name=request.POST['register-username']
            now_password=request.POST['register-password']
            user = User.objects.filter(user_name=now_user_name)
            if user.count()==0:
                new_user=User(user_name=now_user_name,password=now_password)
                new_user.save()
                return HttpResponse("注册成功！")
            else:
                return HttpResponse("用户名已存在！注册失败！")
    return render(request,"login.html")