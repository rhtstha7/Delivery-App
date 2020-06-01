"""registers models to django admin site"""

from django.contrib import admin
from deliveryAppApp.models import Vendor, Customer, Driver


# Register your models here.
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    """Registers vendor model to admin panel"""

    list_display = ('user', 'name', 'phone', 'address')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Registers customer model to admin panel"""

    list_display = ('user', 'avatar', 'phone', 'address')


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    """Registers driver model to admin panel"""

    list_display = ('user', 'avatar', 'phone', 'address')
