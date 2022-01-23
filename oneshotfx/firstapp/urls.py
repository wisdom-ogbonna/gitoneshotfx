from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.index, name='index'),
    path('review/', views.review, name='review'),
    path('contact/', views.contact, name='contact'), 
    path('price/', views.price, name='price'), 
    path('course/', views.course, name='course'), 
    path('SignUp/', views.Signup, name='Signup'), 
    path('teacher/', views.teacher, name='teacher'),
    path('join/', views.join, name='join'),
    #path('price/home/', views.price, name='price/home'),
    #path('price/course/', views.course, name='price/course'), 
    #path('price/price/', views.price, name='price/price'), 
    #path('price/review/', views.review, name='price/review'), 
    #path('price/contact/', views.contact, name='price/contact'), 
]