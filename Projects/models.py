from django.db import models

# Create your models here.
class Product(models.Model):
    p_title = models.CharField(max_length=50);
    p_desc = models.TextField();
    p_github = models.CharField(max_length=50);
    p_img = models.ImageField(upload_to="images");
    p_website = models.CharField(max_length=50);
    p_category = models.CharField(max_length=50, default='');
