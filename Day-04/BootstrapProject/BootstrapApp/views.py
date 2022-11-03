from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'html/home.html')

def contact(request):
	return render(request,'html/contact.html')

def about(request):
	return render(request,'html/about.html')