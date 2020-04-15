#!/user/bin/env python
# 每天都要有好心情
from rest_framework import viewsets

from config.models import Link, SideBar
from config.serializers import LinkSerializer, SideBarSerializer


class LinkViewSet(viewsets.ModelViewSet):
    serializer_class = LinkSerializer
    queryset = Link.objects.filter(status=Link.STATUS_NORMAL)


class SideBarViewSet(viewsets.ModelViewSet):
    serializer_class = SideBarSerializer
    queryset = SideBar.objects.filter(status=SideBar.STATUS_SHOW)
