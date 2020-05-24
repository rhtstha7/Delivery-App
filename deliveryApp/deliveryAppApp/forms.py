from django import forms
from django.contrib.auth.models import User
from deliveryAppApp.models import Vendor

class OwnerForm(forms.ModelForm):
  email = forms.CharField(max_length=100, required=True)
  password = forms.CharField(widget=forms.PasswordInput())

  class Meta:
    model = User
    fields = ("username", "password", "first_name", "last_name", "email")


class VendorForm(forms.ModelForm):
  class Meta:
    model = Vendor
    fields = ("name", "phone", "address", "logo")
