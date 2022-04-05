
from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to = 'images')