from django.contrib import admin
from django.urls import path,include
from mainapp import  views
urlpatterns = [
    path("login/",views.custom_login),
    path("registration/",views.registration_view,name= "register")
]
