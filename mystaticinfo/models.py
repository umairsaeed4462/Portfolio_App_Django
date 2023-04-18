from django.db import models

# Create your models here.
class MyStaticInfo(models.Model):
    my_off_no = models.CharField(max_length=50);
    my_off_email = models.CharField(max_length=50);
    my_off_address = models.CharField(max_length=50);
    my_cv = models.FileField(upload_to="CV/", max_length=300, null=True, default=None)
