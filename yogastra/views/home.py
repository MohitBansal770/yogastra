from django.http import HttpResponse
from django.shortcuts import render
from pathlib import Path

def home(request):
    return (render(request,'C:/Users/Samarth Parnami/Downloads/Yoga-Registration/Front/registration.html'))