from rest_framework import routers
from .api import ConcViewSet

router = routers.DefaultRouter()
router.register('api/conc',ConcViewSet,'conc')

urlpatterns = router.urls