from django.urls import path
from . import views
urlpatterns = [
	path('',views.home,name="hm"),
	path('contactpage/',views.contact,name="cnt"),
	path('aboutpage/',views.about,name="abt"),
]