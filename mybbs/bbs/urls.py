from django.urls import path
from . import views

app_name = 'bbs'
urlpatterns = [
    path("post/", views.post),
    path("posts/",views.posts),
    path("login/",views.login),
]