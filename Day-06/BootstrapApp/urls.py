from django.urls import path
from . import views
from django.contrib.auth import views as ad

urlpatterns = [
	path('',views.home,name="hm"),
	path('contactpage/',views.contact,name="cnt"),
	path('aboutpage/',views.about,name="abt"),
	path('streg/',views.stdntreg,name="strg"),
	path('stupd/<int:h>/',views.stdntup,name="stup"),
	path('stdl/<int:w>/',views.stdlte,name="stdt"),
	path('regp/',views.reg,name="rg"),
	path('loginpage/',ad.LoginView.as_view(template_name="html/login.html"),name="lg"),
	path('logoutpage/',ad.LogoutView.as_view(template_name="html/logout.html"),name="lgo"),
]