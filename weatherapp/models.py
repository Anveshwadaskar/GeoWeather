from django.db import models
from django.contrib.gis.db import models



class Location(models.Model):
    points = models.PointField()

# Create your models here.
