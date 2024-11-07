from . import views
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.landingpage, name='landingpage'),  
    path('homepage/', views.homepage, name='homepage'),
    path('adminhomepage/', views.adminhomepage, name='adminhomepage'),

    # sign up and login
    path('signup/', views.usersignup, name='usersignup'),
    path('login/', views.userlogin, name='userlogin'),
    path('userconfirmlogout/', views.userconfirmlogout, name='userconfirmlogout'),
    path('logout/', views.userlogout, name='userlogout'),
    path ('forgotpassword/', views.forgotpassword, name='forgotpassword'),

    path ('about/', views.about, name='about'),
    path ('contact/', views.contact, name='contact'),
    path ('survey/', views.survey, name='survey'),
    path ('donation/', views.donation, name='donation'),


    
]
