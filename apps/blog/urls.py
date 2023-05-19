from rest_framework import routers

from .views import PostViewSet, TagViewSet

router = routers.DefaultRouter()

router.register(r'posts', PostViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = router.urls
