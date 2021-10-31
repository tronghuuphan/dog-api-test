from rest_framework.routers import DefaultRouter
from . import views 

router = DefaultRouter()
router.register('breeds', views.BreedViewSet)
router.register('dog', views.DogViewSet)

urlpatterns = router.urls