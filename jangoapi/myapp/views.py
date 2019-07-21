from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Spot
from .renderers import SpotJSONRenderer
from .serializers import SpotListSerializer, SpotSerializer


class SpotListApiView(ListAPIView):
  model = Spot
  queryset = Spot.objects.all()
  permission_classes = (AllowAny,)
  renderer_classes = (SpotJSONRenderer,)
  serializer_class = SpotListSerializer


class SpotRetrieveApiView(RetrieveAPIView):
  permission_classes = (AllowAny,)
  renderer_classes = (SpotJSONRenderer,)
  serializer_class = SpotSerializer
  
  def retrieve(self, request, spot_id, *args, **kwargs):
    spot = Spot.objcts.get(id=spot_id)
    serializer = self.serializer_class(spot)
    return Response(serializer.data, status=status.HTTP_200_OK)