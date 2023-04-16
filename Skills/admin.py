from django.contrib import admin
from Skills.models import Skill
# Register your models here.

class SkillAdmin(admin.ModelAdmin):
    list_display = ['skill_title', 'skill_percentage', 'skill_category']

admin.site.register(Skill, SkillAdmin);
