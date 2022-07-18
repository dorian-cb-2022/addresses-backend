from django.contrib import admin

from addresses_tenant.models import Address

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('address_name', 'latitude', 'longitude',)
