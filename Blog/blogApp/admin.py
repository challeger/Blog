from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from blogApp.models import Category, Tag, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_nav', 'owner', 'created_time', 'posts_count')
    fields = ('name', 'status', 'is_nav')

    def posts_count(self, obj):
        return obj.post_set.count()

    posts_count.short_description = '文章数量'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_time', 'owner')
    fields = ('name', 'status')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'category', 'status',
        'created_time', 'operator',
    ]
    list_display_links = []
    
    list_filter = ['category', ]  # 页面过滤器
    search_fields = ['title', 'category__name']  # 配置搜索字段
    
    actions_on_top = True
    actions_on_bottom = True
    
    # 编辑页面
    save_on_top = True  # 把保存,编辑,编辑并新建按钮展示在顶部
    
    fields = (
        ('category', 'title'),
        'desc',
        'status',
        'content',
        'tag',
    )
    
    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('admin:blogApp_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'
    
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)
