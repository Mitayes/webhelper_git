"""webhelper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from ogzn.views import index, start, send_kad_num, search, json_Search, congratulations

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name='home'),
    path('json_Search', json_Search),
    path('admin/', admin.site.urls),
    path('start', start, name='start'),
    path('search', search, name='search'),
    path('send_kad_num', send_kad_num, name='send_kad_num'),
    path('congratulations', congratulations, name='congratulations'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
