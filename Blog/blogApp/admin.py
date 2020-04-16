from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.urls import reverse
from django.utils.html import format_html

from Blog.base_admin import BaseOwnerAdmin
from Blog.custom_site import custom_site

from blogApp.adminforms import PostAdminForm
from blogApp.models import Category, Tag, Post


# class PostInline(admin.TabularInline):
#     fields = ('title', 'desc')
#     extra = 1
#     model = Post


@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'is_nav', 'owner', 'created_time', 'posts_count')
    fields = ('name', 'status', 'is_nav')
    search_fields = ('name', 'id')

    # inlines = [PostInline, ]  # 在同一页面编辑关联数据

    def posts_count(self, obj):
        return obj.post_set.count()

    posts_count.short_description = '文章数量'


@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time', 'owner')
    fields = ('name', 'status')
    search_fields = ('name', 'id')


class CategoryOwnerFilter(admin.SimpleListFilter):
    """自定义过滤器只展示当前用户分类"""

    title = '分类过滤器'  # 标题
    parameter_name = 'owner_category'  # 查询时URL参数的名字

    def lookups(self, request, model_admin):  # 返回要展示的内容和查询用的id
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    list_display = [
        'title', 'category', 'status',
        'created_time', 'operator',
    ]
    list_display_links = []
    
    list_filter = [CategoryOwnerFilter]  # 页面过滤器
    search_fields = ['title', 'category__name']  # 配置搜索字段
    autocomplete_fields = ['category', 'tag']
    
    actions_on_top = True
    actions_on_bottom = True
    
    # 编辑页面
    save_on_top = True  # 把保存,编辑,编辑并新建按钮展示在顶部

    fieldsets = (
        ('基础配置', {
            'description': '基础配置描述',
            'fields': (
                ('title', 'category'),
                'status',
            ),
        }),
        ('内容', {
            'description': '摘要默认选取内容中的前140个字',
            'fields': (
                'desc',
                'is_md',
                'content_ck',
                'content_md',
                'content',
            ),
        }),
        ('额外信息', {
            'classes': ('wide', ),
            'fields': ('tag', ),
        }),
    )

    filter_vertical = ('tag', )
    
    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blogApp_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            kwargs['queryset'] = Category.objects.filter(owner=request.user)
        elif db_field.name == 'tag':
            kwargs['queryset'] = Tag.objects.filter(owner=request.user)
        
        return super(PostAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    # class Media:
    #     css = {
    #         'all': ("https://cdn.bootcss.com/twitter-bootstrap/4.3.1/css/bootstrap.min.css", ),
    #     }
    #     js = ("https://cdn.bootcss.com/twitter-bootstrap/4.4.0/js/bootstrap.bundle.js", 'js/post_editor.js')


@admin.register(LogEntry, site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr', 'object_id', 'action_flag', 'user', 'change_message']
