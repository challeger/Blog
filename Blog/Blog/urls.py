"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps import views as sitemap_views
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from Blog.autocomplete import CategoryAutoComplete, TagAutoComplete
from Blog.custom_site import custom_site
from blogApp.apis import PostViewSet, CategoryViewSet, TagViewSet
from blogApp.rss import LatestPostFeed
from blogApp.sitemap import PostSitemap
from comment.apis import CommentViewSet
from config.apis import LinkViewSet, SideBarViewSet

router = DefaultRouter()
router.register(r'post', PostViewSet, basename='api-post')
router.register(r'category', CategoryViewSet, basename='api-category')
router.register(r'tag', TagViewSet, basename='api-tag')
router.register(r'comment', CommentViewSet, basename='api-comment')
router.register(r'link', LinkViewSet, basename='api-link')
router.register(r'sidebar', SideBarViewSet, basename='api-sidebar')


urlpatterns = [
    path('admin/', custom_site.urls),
    path('super_admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls, name='xadmin'),
    path('config/', include('config.urls', namespace='config')),
    path('comment/', include('comment.urls', namespace='comment')),
    path('rss/', LatestPostFeed(), name='rss'),
    path('sitemap.xml/', sitemap_views.sitemap, {'sitemaps': {'posts': PostSitemap}}),
    path('category-autocomplete/', CategoryAutoComplete.as_view(), name='category-autocomplete'),
    path('tag-autocomplete/', TagAutoComplete.as_view(), name='tag-autocomplete'),
    path('api/', include((router.urls, 'api'))),
    path('api/docs/', get_schema_view(title='My Project')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^', include('blogApp.urls', namespace='blog')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
