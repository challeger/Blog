#!/user/bin/env python
# 每天都要有好心情
from django.urls import path

from comment import views

app_name = 'comment'
urlpatterns = [
    path('', views.CommentView.as_view(), name='commentView'),
]
