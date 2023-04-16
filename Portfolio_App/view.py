from django.http import HttpResponse as http
from django.shortcuts import render
from home.models import home
from Services.models import Services
from myskills.models import MySkill
from Projects.models import Product
from Abouts.models import About
from userauth.models import User

def homePage(req):
    homeData = home.objects.all();
    servicesData = Services.objects.all();
    webSkill = MySkill.objects.filter(skill_category='web').values();
    androidSkill = MySkill.objects.filter(skill_category='android').values();
    webProjects = Product.objects.filter(p_category='web').values();
    androidProjects = Product.objects.filter(p_category='android').values();
    aboutData = About.objects.all();
    userData = User.objects.all();
    data = {
        'homeData':homeData,
        'servicesData': servicesData,
        'webSkill': webSkill,
        'androidSkill': androidSkill,
        'webProjects': webProjects,
        'androidProjects': androidProjects,
        'aboutData': aboutData,
        'userData': userData
    }

    return render(req, "index.html", data);