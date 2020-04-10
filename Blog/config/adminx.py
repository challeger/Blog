#!/user/bin/env python
# 每天都要有好心情
import xadmin
from django.contrib import admin

from Blog.base_xadmin import BaseOwnerAdmin
from Blog.custom_site import custom_site
from config.models import Link, SideBar


@xadmin.sites.register(Link)
class LinkAdmin(BaseOwnerAdmin):
    list_display = ('title', 'href', 'status', 'weight', 'created_time')
    fields = ('title', 'href', 'status', 'weight')


@xadmin.sites.register(SideBar)
class SideBarAdmin(BaseOwnerAdmin):
    list_display = ('title', 'display_type', 'content', 'created_time')
    fields = ('title', 'display_type', 'content')
