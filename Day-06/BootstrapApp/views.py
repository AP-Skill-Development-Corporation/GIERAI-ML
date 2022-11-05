from django.shortcuts import render,redirect
from . models import Student
from . forms import UsRegister
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
@login_required
def home(request):
	return render(request,'html/home.html')

def contact(request):
	return render(request,'html/contact.html')

def about(request):
	return render(request,'html/about.html')

@login_required
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

def stdntup(request,h):
	m = Student.objects.get(id=h)
	if request.method == "POST":
		m.stroll = request.POST['sr']
		m.stname = request.POST['sn']
		m.stbranch = request.POST['sb']
		m.styear = request.POST['sy']
		m.save()
		return redirect('/streg')
	return render(request,'html/stdupdate.html',{'b':m})

def stdlte(request,w):
	c = Student.objects.get(id=w)
	if request.method == "POST":
		c.delete()
		return redirect('/streg')
	return render(request,'html/stdlte.html',{'z':c})

def reg(request):
	if request.method == "POST":
		s = UsRegister(request.POST)
		if s.is_valid():
			s.save()
			messages.success(request,"User Created Successfully")
			return redirect('/loginpage')
	s = UsRegister()
	return render(request,'html/regis.html',{'u':s})
