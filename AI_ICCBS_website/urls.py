"""AI_ICCBS_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.contrib.auth.models import User


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AI_ICCBS_website.apps.public.urls')),
    path('accounts/', include('AI_ICCBS_website.apps.accounts.urls')),
    path('contact/', include('AI_ICCBS_website.apps.contact.urls')),
    path('blog/', include('AI_ICCBS_website.apps.blog.urls')),   
    path('ckeditor/', include('ckeditor_uploader.urls')), 
    path('ticketApp/', include("AI_ICCBS_website.apps.ticketApp.urls")),
]   

if settings.DEBUG:
       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 


 
  



