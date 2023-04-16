from django.db import models

# Create your models here.
class Skill(models.Model):
    skill_title = models.CharField(max_length=50);
    skill_percentage = models.CharField(max_length=50);
    skill_category = models.CharField(max_length=50);