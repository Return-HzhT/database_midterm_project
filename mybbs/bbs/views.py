from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from bbs.models import *
# Create your views here.
def post(request,post_id):
    post_id=int(post_id)
    context={}
    context['title']=Post.objects.get(id=post_id).title
    context['body']=Post.objects.get(id=post_id).body
    return render(request,"post.html",context)

def posts(request):
    if request.method=='POST' and request.POST:
        now_post_id=request.POST['id']
        return HttpResponseRedirect("/post/"+now_post_id)
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
                user_id=user.id
                if user.password==now_password:
                    return HttpResponseRedirect("/user_home/"+str(user_id))
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

def user_home(request,user_id):
    if request.method=='POST' and request.POST:
        if request.POST['action']=='view_details':
            now_post_id=request.POST['id']
            return HttpResponseRedirect("/post/"+now_post_id)
        elif request.POST['action']=='new_post':
            new_post_title=request.POST['post-title']
            new_post_content=request.POST['post-content']
            author_user=User.objects.get(id=user_id)
            new_post = Post(title=new_post_title,body=new_post_content,author=author_user)
            new_post.save()
            return HttpResponse("成功发布新帖子！")
        elif request.POST['action']=='view_all_posts':
            return HttpResponseRedirect("/posts/")
    user_id=int(user_id)
    context={}
    context['my_posts']=Post.objects.filter(author=user_id)
    return render(request,"user_home.html",context)