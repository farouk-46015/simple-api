from rest_framework import routers
from .views import CarViewSet , RateViewSet , PopularViewSet

router = routers.DefaultRouter()
router.register('cars',CarViewSet,basename='card')
router.register('rate',RateViewSet,basename='rate')
router.register('popular',PopularViewSet,basename='popular')


urlpatterns = router.urls
