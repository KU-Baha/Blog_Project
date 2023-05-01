from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .models import Post, Tag
from .serializers import PostSerializer, TagSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.AllowAny]
