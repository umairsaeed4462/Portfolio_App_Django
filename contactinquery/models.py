from django.db import models

class ContactInquery(models.Model):
    user_name = models.CharField(max_length=50);
    user_email = models.CharField(max_length=50);
    user_project = models.CharField(max_length=50);
    user_message = models.TextField();

# Create your models here.