from rest_framework import routers
from .api import CategoriaViewSet, MensajeViewSet

router = routers.DefaultRouter()

router.register('api/categoria', CategoriaViewSet, 'categoria')
router.register('api/mensaje', MensajeViewSet, 'mensaje')

urlpatterns = router.urls