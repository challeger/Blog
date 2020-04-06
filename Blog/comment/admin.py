from django.contrib import admin

from Blog.base_admin import BaseOwnerAdmin
from Blog.custom_site import custom_site
from comment.models import Comment


@admin.register(Comment, site=custom_site)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')
