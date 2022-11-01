from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fj(e):
	return HttpResponse("Good Afternoon to All..")

def qw(r,y):
	return HttpResponse(f"Hi welcome {y}")

def bi(r,x,z):
	return HttpResponse(f"<h1>student name is : {x}<br>student age is:{z}</h1>")
	