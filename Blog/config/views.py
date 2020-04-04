from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic import ListView

from blogApp.views import CommonViewMixin
from config.models import Link


def links(request):
    return HttpResponse('links')


class LinkListView(CommonViewMixin, ListView):
    queryset = Link.objects.filter(status=Link.STATUS_NORMAL)
    template_name = 'config/links.html'
    context_object_name = 'link_list'
