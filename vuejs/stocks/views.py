import os
from django.conf import settings
from django.http.response import HttpResponse
from rest_framework import viewsets
from .models import Stock
from .serializers import StockSerializer

def index(_):
  html = open(os.path.join(settings.STATICFILES_DIRS[0], 'vue_grid.html')).read()
  return HttpResponse(html)

class StockViewSet(viewsets.ModelViewSet):
  queryset = Stock.objects.all()
  serializer_class = StockSerializer
  filter_fields = ('id', 'title', 'stock_count')