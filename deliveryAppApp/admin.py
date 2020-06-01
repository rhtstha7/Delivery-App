"""registers models to django admin site"""

from django.contrib import admin
from deliveryAppApp.models import Vendor


# Register your models here.
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    """Registers vendor model to admin panel"""

    list_display = ('user', 'name', 'phone', 'address')
