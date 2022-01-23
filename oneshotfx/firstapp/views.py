from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def review(request):
    return render(request, 'review.html')

def price(request):
    return render(request, 'price.html')

def contact(request):
    return render(request, 'contact.html')

def course(request):
    return render(request, 'course.html')

def Signup(request):
    return render(request, 'Signup.html')

def teacher(request):
    return render(request, 'teacher.html')

def join(request):
    return render(request, 'join.html', {})









    

    



