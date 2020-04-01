#!/user/bin/env python
# 每天都要有好心情
from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_title = 'Blog管理后台'
    site_header = 'Blog'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')
