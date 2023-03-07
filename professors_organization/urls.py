from rest_framework import routers

from .api import GroupViewSet

router = routers.DefaultRouter()

router.register('groups', GroupViewSet, 'groups'),


urlpatterns = router.urls