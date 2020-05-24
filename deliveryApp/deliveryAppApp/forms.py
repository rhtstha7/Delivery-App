from django import forms
from django.contrib.auth.models import User
from deliveryAppApp.models import Vendor

class OwnerForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ("username", "password", "first_name", "last_name", "email")


class VendorForm(forms.ModelForm):
  class Meta:
    model = Vendor
    fields = ("name", "phone", "address", "logo")
