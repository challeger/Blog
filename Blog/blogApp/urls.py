#!/user/bin/env python
# 每天都要有好心情
from django.contrib import admin
from django.urls import path, re_path

from blogApp import views

app_name = 'blog'
urlpatterns = [
    path('category/<int:category_id>/', views.CategoryView.as_view(), name='category-list'),
    path('tag/<int:tag_id>/', views.TagView.as_view(), name='tag-list'),
    path('post/<int:post_id>.html', views.PostDetailView.as_view(), name='post-detail'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('author/<int:owner_id>/', views.AuthorView.as_view(), name='author'),
    re_path(r'^', views.IndexView.as_view(), name='post_list'),
]
