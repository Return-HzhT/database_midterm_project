from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from bbs.models import *
# Create your views here.
def post(request,post_id):
    user_id=int(request.session['bbs_user_id'])
    post_id=int(post_id)
    if request.method=='POST' and request.POST:
        if request.POST['action']=='favorite':
            now_user=User.objects.get(id=user_id)
            now_post=Post.objects.get(id=post_id)
            favorite=Favorite(user=now_user,post=now_post)
            favorite.save()
            return HttpResponse("收藏成功！")
        elif request.POST['action']=='cancel_favorite':
            favorite=Favorite.objects.filter(user=user_id).get(post=post_id)
            favorite.delete()
            return HttpResponse("已取消收藏！")
    context={}
    context['title']=Post.objects.get(id=post_id).title
    context['body']=Post.objects.get(id=post_id).body
    favorite=Favorite.objects.filter(user=user_id).filter(post=post_id)
    if favorite.count()==0:
        context['favorite']=False
    else:
        context['favorite']=True
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
                    request.session['bbs_user_id']=user_id
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
        elif request.POST['action']=='view_all_posts':
            return HttpResponseRedirect("/posts/")
        elif request.POST['action']=='delete':
            now_post_id=int(request.POST['id'])
            now_post=Post.objects.get(id=now_post_id)
            now_post.delete()
    user_id=int(user_id)
    context={}
    context['my_id']=user_id
    context['my_posts']=Post.objects.filter(author=user_id)
    return render(request,"user_home.html",context)

def favorite(request,user_id):
    if request.method=='POST' and request.POST:
        if request.POST['action']=='view_details':
            now_post_id=request.POST['id']
            return HttpResponseRedirect("/post/"+now_post_id)
    user_id=int(user_id)
    context={}
    favorite_list=list(Favorite.objects.filter(user=user_id).values_list("post",flat=True))
    if len(favorite_list)==0:
        return HttpResponse("没有收藏的帖子！")
    context['posts']=[]
    for post_id in favorite_list:
        context['posts'].append(Post.objects.get(id=post_id))
    return render(request,"favorite.html",context)