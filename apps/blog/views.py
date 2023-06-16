from django.views import View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, filters as rest_filters
from django_filters import rest_framework as filters

from .models import Category, Post, Tag, BannedWord
from .serializers import CategorySerializer, PostSerializer, TagSerializer, BannedWordSerializer
from .tasks import create_banned_word


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
    filter_backends = [
        filters.DjangoFilterBackend,
        rest_filters.SearchFilter,
        rest_filters.OrderingFilter,
    ]
    filterset_fields = [
        'category',
        'tags',
    ]
    search_fields = [
        'title',
        'content',
        'author',
    ]
    ordering_fields = [
        'pub_date',
        'update_date',
    ]


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]


class BannedWordViewSet(ModelViewSet):
    queryset = BannedWord.objects.all()
    serializer_class = BannedWordSerializer
    permission_classes = [permissions.IsAdminUser]


class RunParser(View):
    def get(self, request, date):
        create_banned_word.delay(date)
        return JsonResponse({'status': 'ok'}, status=200)
