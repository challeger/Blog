#!/user/bin/env python
# 每天都要有好心情
from django.contrib import admin
from django.urls import path, re_path

from blogApp import views

app_name = 'blog'
urlpatterns = [
    path('category/<int:category_id>/', views.post_list, name='category'),
    path('tag/<int:tag_id>/', views.post_list, name='tag'),
    path('post/<int:post_id>.html', views.post_detail, name='post'),
    re_path(r'^', views.post_list, name='post_list'),
]
