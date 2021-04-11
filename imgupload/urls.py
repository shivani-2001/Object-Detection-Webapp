from django.contrib import admin
from django.urls import re_path, include, path
from imgupload import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path('imageprocess', views.imageprocess, name='imageprocess')
]