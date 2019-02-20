"""enlacerv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.generic.list import ListView
#from django.conf.urls import url, include
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from usuarios import views as usuarios_views
from contact import views as contact_views

#app_name = 'enlacerv'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', usuarios_views.Home.as_view(), name='home'),
    path('about/', usuarios_views.about, name='about'),
    path('contact/', contact_views.contact, name='contact'),
    path('manuales/', usuarios_views.manuales, name='manuales'),
    path('profile/', usuarios_views.view_profile, name='profile'),
    path('edit-profile/', usuarios_views.edit_profile, name='edit-profile'),
    path('accounts/', include('allauth.urls')),
    path('avatar/', include('avatar.urls')),
    path('inventario/', include('productos.urls')),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
