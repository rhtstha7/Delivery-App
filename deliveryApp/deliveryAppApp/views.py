from django.shortcuts import render, redirect

# Create your views here.
def home(request):
  return redirect(vendor_home)

def vendor_home(request):
  return render(request, 'vendor/home.html')
