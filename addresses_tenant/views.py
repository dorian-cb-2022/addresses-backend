from django.shortcuts import render
from django.conf import settings
from .models import Address

def address_detail(request):
    address_objs = Address.objects.all()

    context = {
        "addresses": address_objs,
    }

    return render(request, 'addresses_tenant/map.html', context)