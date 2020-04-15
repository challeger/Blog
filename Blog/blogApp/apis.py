#!/user/bin/env python
# 每天都要有好心情
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser

from blogApp.models import Post, Category, Tag
from blogApp.serializers import (
    PostSerializer, PostDetailSerializer,
    CategorySerializer, CategoryDetailSerializer,
    TagSerializer, TagDetailSerializer)


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
    permission_classes = [IsAdminUser]  # 写入时的权限校验

    def list(self, request, *args, **kwargs):  # 获取列表时
        self.serializer_class = PostSerializer
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):  # 获取单个对象时
        self.serializer_class = PostDetailSerializer
        return super().retrieve(request, *args, **kwargs)

    def filter_queryset(self, queryset):
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(status=Category.STATUS_NORMAL)

    def list(self, request, *args, **kwargs):  # 获取列表时
        self.serializer_class = CategorySerializer
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):  # 获取单个对象时
        self.serializer_class = CategoryDetailSerializer
        return super().retrieve(request, *args, **kwargs)


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.filter(status=Tag.STATUS_NORMAL)

    def list(self, request, *args, **kwargs):  # 获取列表时
        self.serializer_class = TagSerializer
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):  # 获取单个对象时
        self.serializer_class = TagDetailSerializer
        return super().retrieve(request, *args, **kwargs)
