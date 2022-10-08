"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('registration', views.registration, name='registration'),
    path('image_upload', views.hotel_image_view, name='image_upload'),
    path('success', views.success, name='success'),
    path('basic_data', views.basic_data, name='basic_data'),
    path('certificates', views.certificates, name='certificates'),
    path('skills', views.skills, name='skills'),
    path('education', views.education, name='education'),
    path('work_experience', views.work_experience, name='work_experience'),
    path('social_media', views.social_media, name='social_media'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
