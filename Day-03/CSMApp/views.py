from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fj(e):
	return HttpResponse("Good Afternoon to All..")

def qw(r,y):
	return HttpResponse(f"Hi welcome {y}")

def bi(r,x,z):
	return HttpResponse(f"<h1>student name is : {x}<br>student age is:{z}</h1>")
	
def ar(b):
	return HttpResponse("<html><head><title>Demo</title></head><body><h3>Sample Html Structure in HttpResponse</h3></body></html>")

def yp(g,n):
	return HttpResponse(f"<html><head><title>Example</title></head><body><h3>Sample Data from url {n}</h3></body></html>")

def vh(k,nm):
	return HttpResponse("<html><head><title>Example</title><style>h3{background-color:green}</style></head><body><h3>Sample Data from url <span style='color:white'>"+nm+"</span></h3></body></html>")

def bk(t,dm):
	return HttpResponse(f"<html><head><title>Javascript</title><script>alert('Hi Welcome {dm}');</script></head><body><h3>Sample Data from url for javascript {dm}</h3></body></html>")

def sa(q):
	return render(q,'sample.html')

def nk(a,sn,sy,sr):
	return render(a,'demo.html',{'name':sn,'roll':sr,'year':sy})

def stdnt(request):
	if request.method == "POST":
		a = request.POST['sn']
		b = request.POST['sr']
		c = request.POST['sb']
		d = request.POST['sy']
		print(a,b,c,d)
	return render(request,'stdreg.html')



