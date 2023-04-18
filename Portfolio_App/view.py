from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from home.models import home
from Services.models import Services
from myskills.models import MySkill
from Projects.models import Product
from Abouts.models import About
from userauth.models import User
from contactinquery.models import ContactInquery
from django.core.mail import send_mail
from validate_email import validate_email

from django.core.validators import validate_email as vm

isValue = 1

contentString = ""

def homePage(req):


    global contentString, isValue
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
        'userData': userData,
        'isHome': isValue,
        'status': contentString
    }

    contentString = ""
    isValue = 1    
    return render(req, "index.html", data);

def contactus(req):
    global isValue
    global contentString
    

    try:
        
        name = req.POST.get('name')
        email = req.POST.get('email')
        project = req.POST.get('project')
        message = req.POST.get('message')
        is_valid = validate_email(email)
        if (is_valid == False):
            contentString = "Email Not Valid"
        else:
            #send to user
            send_mail(
                "Umair Saeed",
                "Hi," + name + " THANKS YOU! Please send more detail about you query",
                'mumairsaeed4462@gmail.com',
                [email],
                fail_silently=False,
            )
            # send to me
            send_mail(
                project + " EMAIL: " + email,
                "Hi, Umair my name is " + name + " and my Query is '" + message + "'",
                email,
                ["mumairsaeed4462@gmail.com"],
                fail_silently=False,
            )
            contentString = "Sucessfully Submitted"
            data = ContactInquery(user_name=name, user_email=email, user_project=project, user_message=message)
            data.save()

        
    except:
        contentString = "Something Want Wrong!"
    
    isValue = 0
    return HttpResponseRedirect("/");