from django.shortcuts import render
from django.conf import settings
from .models import Address

def address_detail(request):
    address_objs = Address.objects.get()

    context = {
        "addresses": address_objs,
    }

    return render(request, 'addresses_tenant/map.html', context)

def map(request):

	name = request.GET.get("name")
	lat = request.GET.get("lat")
	lon = request.GET.get("lon")

	print(name)

	context = {
	"google_api_key": settings.GOOGLE_API_KEY,
	"lat": lat,
	"lon": lon,
	}
    
	return render(request, 'addresses_tenant/map.html', context)