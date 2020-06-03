"""deliveryApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from deliveryAppApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('vendor/sign-in',
         auth_views.LoginView.as_view(template_name='vendor/sign_in.html'),
         name='vendor-sign-in'),
    path('vendor/sign-out', auth_views.LogoutView.as_view(),
         {'next_page': '/'},
         name='vendor-sign-out'),
    path('vendor/sign-up', views.vendor_sign_up,
         name='vendor-sign-up'),
    path('vendor/', views.vendor_home, name='vendor-home'),
    path('api/social/', include('rest_framework_social_oauth2.urls')),

    path('vendor/account/', views.vendor_account,
         name='vendor-account'),
    path('vendor/item/', views.vendor_item,
         name='vendor-item'),
    path('vendor/order/', views.vendor_order,
         name='vendor-order'),
    path('vendor/report/', views.vendor_report,
         name='vendor-report'),

    # /convert-token(sign in/ sign up)
    # /revoke-token(sign out)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
