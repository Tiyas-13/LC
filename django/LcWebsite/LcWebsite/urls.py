"""LcWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from MUN import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('land/', v.landing, name='land'),
    path('', v.base, name = 'home'),
    path('committee/',v.committee, name = 'register'),
    path('ip/',v.ip, name = 'register2'),
    path('thankyou/',v.thank, name='thankyou'),
]
