from django.contrib import admin
from Projects.models import Product
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['p_title','p_desc','p_github', 'p_img', 'p_website', 'p_category'];

admin.site.register(Product, ProjectAdmin);