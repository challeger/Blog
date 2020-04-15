#!/user/bin/env python
# 每天都要有好心情
from rest_framework import serializers

from config.models import Link, SideBar


class LinkSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:api-link-detail')
    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        model = Link
        fields = '__all__'


class SideBarSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:api-sidebar-detail')
    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        model = SideBar
        fields = '__all__'
