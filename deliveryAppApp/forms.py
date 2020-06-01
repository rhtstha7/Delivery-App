"""forms for deliveryAppApp"""

from django import forms
from django.contrib.auth.models import User
from deliveryAppApp.models import Vendor

class OwnerForm(forms.ModelForm):
    """form for the owner of the business"""

    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        """specifies model and fields"""
        model = User
        fields = ("username", "password", "first_name", "last_name", "email")


class VendorForm(forms.ModelForm):
    """form for the vender/business"""
    
    class Meta:
        """specifies model and fields"""
        model = Vendor
        fields = ("name", "phone", "address", "logo")
