"""models for deliveryAppApp"""

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Vendor(models.Model):
    """Vendor model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='vendor')
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='vendor_logo/', blank=False)

    def _str__(self):
        return self.name


class Customer(models.Model):
    """Customer model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='customer')
    avatar = models.CharField(max_length=500)
    phone = models.CharField(max_length=500, blank=True)
    address = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.user.get_full_name()


class Driver(models.Model):
    """Driver model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='driver')
    avatar = models.CharField(max_length=500)
    phone = models.CharField(max_length=500, blank=True)
    address = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.user.get_full_name()
