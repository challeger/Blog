#!/user/bin/env python
# 每天都要有好心情
import xadmin
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.urls import reverse
from django.utils.html import format_html
from xadmin.layout import Row, Fieldset
from xadmin.filters import manager, RelatedFieldListFilter

from Blog.base_xadmin import BaseOwnerAdmin
from Blog.custom_site import custom_site

from blogApp.adminforms import PostAdminForm
from blogApp.models import Category, Tag, Post


# class PostInline(admin.TabularInline):
#     fields = ('title', 'desc')
#     extra = 1
#     model = Post


@xadmin.sites.register(Category)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'is_nav', 'owner', 'created_time', 'posts_count')
    fields = ('name', 'status', 'is_nav')

    # inlines = [PostInline, ]  # 在同一页面编辑关联数据

    def posts_count(self, obj):
        return obj.post_set.count()

    posts_count.short_description = '文章数量'


@xadmin.sites.register(Tag)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time', 'owner')
    fields = ('name', 'status')


class CategoryOwnerFilter(RelatedFieldListFilter):
    """自定义过滤器只展示当前用户分类"""

    @classmethod
    def test(cls, field, request, params, model, admin_view, field_path):
        return field.name == 'category'

    def __init__(self, field, request, params, model, model_admin, field_path):
        super(CategoryOwnerFilter, self).__init__(field, request, params, model, model_admin, field_path)
        # 重新获取lookup_choices, 根据owner过滤
        self.lookup_choices = Category.objects.filter(owner=request.user).values_list('id', 'name')


manager.register(CategoryOwnerFilter, take_priority=True)


@xadmin.sites.register(Post)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    list_display = [
        'title', 'category', 'status',
        'created_time', 'operator',
    ]
    exclude = ('owner', 'pv', 'uv')
    list_display_links = []

    list_filter = ['category']  # 页面过滤器
    search_fields = ['title', 'category__name']  # 配置搜索字段

    actions_on_top = True
    actions_on_bottom = True

    # 编辑页面
    save_on_top = True  # 把保存,编辑,编辑并新建按钮展示在顶部

    form_layout = (
        Fieldset(
            '基础信息',
            Row('title', 'category'),
            'status',
            'tag',
        ),
        Fieldset(
            '内容信息',
            'desc',
            'content',
        )
    )

    filter_vertical = ('tag', )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            self.model_admin_url('change', obj.id)
        )
    operator.short_description = '操作'

    # @property
    # def media(self):
    #     media = super().media
    #     media.add_js(['https://cdn.bootcss.com/twitter-bootstrap/4.4.0/js/bootstrap.bundle.js'])
    #     media.add_css({
    #         'all': ('https://cdn.bootcss.com/twitter-bootstrap/4.3.1/css/bootstrap.min.css',),
    #     })
    #     return media
