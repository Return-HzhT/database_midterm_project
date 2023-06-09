from django.urls import path,re_path
from . import views

app_name = 'bbs'
urlpatterns = [
    path("",views.login),
    path("posts/",views.posts),
    path("login/",views.login),
    path("my_home/",views.my_home),
    re_path(r"^post/(?P<post_id>\d{1,10})/$", views.post),
    re_path(r"^user_home/(?P<user_id>\d{1,10})/$",views.user_home),
    re_path(r"^favorite/(?P<user_id>\d{1,10})/$",views.favorite),
    re_path(r"^follow/(?P<user_id>\d{1,10})/$",views.follow),
]