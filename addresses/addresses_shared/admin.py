from django.contrib import admin

from addresses_shared.models import AddressType

@admin.register(AddressType)
class AddressTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
