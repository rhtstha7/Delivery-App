from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Vendor(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vendor')
  name = models.CharField(max_length=500)
  phone = models.CharField(max_length=500)
  address = models.CharField(max_length=500)
  logo = models.ImageField(upload_to='vendor_logo/', blank=False)

  def _str__(self):
    return self.name
