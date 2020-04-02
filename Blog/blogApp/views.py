from django.http import HttpResponse
from django.shortcuts import render

from blogApp.models import Tag, Post, Category
from config.models import SideBar


def post_list(request, category_id=None, tag_id=None):
    tag = None
    category = None

    if tag_id:
        post_lists, tag = Post.get_by_tag(tag_id)
    elif category_id:
        post_lists, category = Post.get_by_category(category_id)
    else:
        post_lists = Post.latest_posts()

    context = {
        'category': category,
        'tag': tag,
        'post_lists': post_lists,
        'sidebars': SideBar.get_all(),
    }
    context.update(Category.get_navs())

    return render(request, 'list.html', context=context)


def post_detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None

    context = {
        'post': post,
        'sidebars': SideBar.get_all(),
    }
    context.update(Category.get_navs())

    return render(request, 'detail.html', context=context)
