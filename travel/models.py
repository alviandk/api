import json

from django.db import models

# Create your models here.

class Province(models.Model):
    name = models.CharField(max_length=245)
    short_description = models.TextField()
    island = models.CharField(max_length=2)
    url = models.URLField()
    
    def __str__(self):
		return self.name


class Destination(models.Model):
    name = models.CharField(max_length=245)
    short_description = models.TextField()
    province = models.ForeignKey(Province, name = "province_name")
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    tagline = models.CharField(max_length=240, blank=True, null=True)
    url = models.URLField()

    def __str__(self):
		return self.name

