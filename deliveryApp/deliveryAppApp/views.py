from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
  return redirect(vendor_home)

@login_required(login_url='/vendor/sign-in')
def vendor_home(request):
  return render(request, 'vendor/home.html', {})

def vendor_sign_up(request):
  return render(request, 'vendor/sign_up.html', {})
