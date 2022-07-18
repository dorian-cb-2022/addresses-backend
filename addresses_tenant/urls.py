from django.urls import path
from . import views


app_name = "addresses_tenant"

urlpatterns = [
	
	path('', views.map, name="map"),

	]