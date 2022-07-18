from django.shortcuts import render
from django.conf import settings

from .mixins import Directions
'''
Basic view for routing 
'''
def route(request):

	context = {"google_api_key": settings.GOOGLE_API_KEY}
	return render(request, 'atenant/route.html', context)

'''
Basic view for displaying a map 
'''
def map(request):

	name = request.GET.get("name")
	lat = request.GET.get("lat")
	lon = request.GET.get("lon")

	context = {
	"google_api_key": settings.GOOGLE_API_KEY,
	"lat": lat,
	"lon": lon,
	}
    
	return render(request, 'atenant/map.html', context)