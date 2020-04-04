#!/user/bin/env python
# 每天都要有好心情
from django.contrib import admin
from django.urls import path

from config import views

app_name = 'config'
urlpatterns = [
    path('links/', views.LinkListView.as_view(), name='links'),
]
