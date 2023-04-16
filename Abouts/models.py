from django.db import models

# Create your models here.
class About(models.Model):
    about_key = models.CharField(max_length=50);
    about_value = models.CharField(max_length=50);