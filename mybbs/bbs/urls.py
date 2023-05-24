from django.urls import path,re_path
from . import views

app_name = 'bbs'
urlpatterns = [
    re_path(r"^post/(?P<post_id>\d{1,10})/$", views.post),
    path("posts/",views.posts),
    path("login/",views.login),
    re_path(r"^user_home/(?P<user_id>\d{1,10})/$",views.user_home),
]