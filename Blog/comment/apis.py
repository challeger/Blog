#!/user/bin/env python
# 每天都要有好心情
from rest_framework import viewsets

from comment.models import Comment
from comment.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.filter(status=Comment.STATUS_NORMAL)
