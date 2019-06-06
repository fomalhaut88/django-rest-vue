from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('persons', views.PersonViewSet)
router.register('countries', views.CountryViewSet)
urlpatterns = router.urls
