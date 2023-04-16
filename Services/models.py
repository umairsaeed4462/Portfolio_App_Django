from django.db import models

class Services(models.Model):
    ser_icon = models.CharField(max_length=50);
    ser_title = models.CharField(max_length=50);
    ser_desc = models.TextField();

# Create your models here.
