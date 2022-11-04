from django.shortcuts import render,redirect
from . models import Student
# Create your views here.
def home(request):
	return render(request,'html/home.html')

def contact(request):
	return render(request,'html/contact.html')

def about(request):
	return render(request,'html/about.html')

def stdntreg(request):
	p = Student.objects.all()
	if request.method == "POST":
		a = request.POST['sr']
		b = request.POST['sn']
		c = request.POST['sb']
		d = request.POST['sy']
		y = Student(stroll=a,stname=b,stbranch=c,styear=d)
		y.save()
		return redirect('/streg')
	return render(request,'html/stdreg.html',{'v':p})