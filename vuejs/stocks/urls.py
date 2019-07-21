from django.conf.urls import include, url
from rest_framework import routers
from .views import StockViewSet, index

router = routers.DefaultRouter()
router.register(r'stock', StockViewSet)

urlpatterns = [
  url(r'api/', include(router.urls)),
  url(r'', index, name='index'),
]