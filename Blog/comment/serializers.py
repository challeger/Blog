#!/user/bin/env python
# 每天都要有好心情
from rest_framework import serializers

from comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:api-comment-detail')

    class Meta:
        model = Comment
        fields = ('url', 'id', 'target', 'content', 'nickname', 'website', 'email', 'created_time')
