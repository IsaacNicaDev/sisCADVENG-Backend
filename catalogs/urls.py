from rest_framework import routers

from .api import SexoViewSet

router = routers.DefaultRouter()

router.register('api/catalogs', SexoViewSet, 'catalogs')

urlpatterns = router.urls