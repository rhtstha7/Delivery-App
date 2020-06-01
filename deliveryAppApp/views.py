"""views for deliveryAppApp"""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from deliveryAppApp.forms import OwnerForm, VendorForm

# Create your views here.
def home(request):
    return redirect(vendor_home)

@login_required(login_url='/vendor/sign-in')
def vendor_home(request):
    return render(request, 'vendor/home.html', {})

def vendor_sign_up(request):
    owner_form = OwnerForm()
    vendor_form = VendorForm()

    if request.method == "POST":
        owner_form = OwnerForm(request.POST)
        vendor_form = VendorForm(request.POST, request.FILES)

        if owner_form.is_valid() and vendor_form.is_valid():
            new_owner = User.objects.create_user(**owner_form.cleaned_data)
            new_vendor = vendor_form.save(commit=False)
            new_vendor.user = new_owner
            new_vendor.save()

            login(request, authenticate(
                username=owner_form.cleaned_data["username"],
                password=owner_form.cleaned_data["password"]
            ))

            return redirect(vendor_home)

    return render(request, 'vendor/sign_up.html', {
        "owner_form": owner_form,
        "vendor_form": vendor_form
  })
