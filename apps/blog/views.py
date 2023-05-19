from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .models import Category, Post, Tag, BannedWord
from .serializers import CategorySerializer, PostSerializer, TagSerializer, BannedWordSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.filter(parent=None)
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        obj = get_object_or_404(Category, pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAdminUser]


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]


class BannedWordViewSet(ModelViewSet):
    queryset = BannedWord.objects.all()
    serializer_class = BannedWordSerializer
    permission_classes = [permissions.IsAdminUser]
