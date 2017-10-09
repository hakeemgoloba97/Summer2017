from django.conf.urls import url
from django.contrib import admin
from mainApp import views


app_name = 'mainApp'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^login/$',views.user_login,name='user_login'),
    url(r'^login/$',views.movieRate,name='movieRate'),
    url(r'^recommendor/$',views.recommendor,name='recommendor'),
]
