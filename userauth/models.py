from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50);
    desc = models.CharField(max_length=50);
    logo = models.ImageField(upload_to="images")
