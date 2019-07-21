from rest_framework import serializers
from .models import Spot

class SpotListSerializer(serializers.ModelSerializer):
  name = serializers.CharField(max_length=50)
  category = serializers.CharField(max_length=5, allow_blank=True)
  address_prefecture = serializers.CharField(max_length=10, allow_blank=True)

  class Meta:
    model = Spot
    fields = ('id', 'name', 'category', 'adress_prefecture')


class SpotSerializer(serializers.ModelSerializer):
  name = serializers.CharField(max_length=50)
  category = serializers.CharField(max_length=5, allow_blank=True)
  genre = serializers.CharField(max_length=50, allow_blank=True)
  address_prefecture = serializers.CharField(max_length=10, allow_blank=True)
  address_city = serializers.CharField(max_length=10, allow_blank=True)
  address_street = serializers.CharField(max_length=100, allow_blank=True)
  latitude = serializers.CharField(max_length=50, allow_blank=True)
  longitude = serializers.CharField(max_length=50, allow_blank=True)

  class Meta:
    model = Spot
    fields = ('name', 'category', 'genre', 'address_prefecture', 'address_city', 'address_street', 'latitude', 'longitude')
