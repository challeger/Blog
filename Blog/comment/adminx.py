#!/user/bin/env python
# 每天都要有好心情
import xadmin
from django.contrib import admin

from comment.models import Comment


@xadmin.sites.register(Comment)
class CommentAdmin:
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')
