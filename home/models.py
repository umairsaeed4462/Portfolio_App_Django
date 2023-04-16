from django.db import models

class home(models.Model):
    home_desc = models.TextField(default="");
    long_desc = models.TextField(default="");

# Create your models here.
