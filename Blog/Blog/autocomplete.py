#!/user/bin/env python
# 每天都要有好心情
from dal import autocomplete

from blogApp.models import Category, Tag


class CategoryAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:  # 判断是否登录
            return Category.objects.none

        qs = Category.objects.filter(owner=self.request.user)

        if self.q:  # 判断url参数上传来的值
            qs = qs.filter(name__istartswith=self.q)

        return qs


class TagAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Tag.objects.none

        qs = Tag.objects.filter(owner=self.request.user)

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs
