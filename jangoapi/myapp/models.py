from django.db import models

class Spot(models.Model):
  name = models.CharField(max_length=50)
  category = models.CharField(max_length=5, blank=True)
  genre = models.CharField(max_length=50, blank=True)
  address_prefecture = models.CharField(max_length=10, blank=True)
  address_city = models.CharField(max_length=10, blank=True)
  address_street = models.CharField(max_length=100, blank=True)
  latitude = models.CharField(max_length=50, blank=True)
  longitude = models.CharField(max_length=50, blank=True)
  longitude = models.CharField(max_length=50, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ('created_at',)