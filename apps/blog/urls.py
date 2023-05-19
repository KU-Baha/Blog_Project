from rest_framework import routers

from .views import CategoryViewSet, PostViewSet, TagViewSet, BannedWordViewSet

router = routers.DefaultRouter()

router.register(r'categories', CategoryViewSet)
router.register(r'posts', PostViewSet)
router.register(r'tags', TagViewSet)
router.register(r'banned-words', BannedWordViewSet)

urlpatterns = router.urls
