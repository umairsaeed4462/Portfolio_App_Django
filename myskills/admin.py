from django.contrib import admin
from myskills.models import MySkill

class MySkillAdmin(admin.ModelAdmin):
    list_display = ['skill_title', 'skill_percentage', 'skill_category']

admin.site.register(MySkill, MySkillAdmin);
# Register your models here.
