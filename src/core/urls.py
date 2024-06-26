"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from rest_framework import routers

from user.api import viewsets as userviewsets

route = routers.DefaultRouter()

route.register(r'user-infos', userviewsets.UserInfoViewSet, basename='UserInfo')
route.register(r'users', userviewsets.UserViewSet, basename='User')
# route.register(r'auth', userviewsets.UserLoginViewSet.as_view(), basename='Auth')
# route.register(r'create-user', userviewsets.UserRegistrationViewSet, basename='CreateUser')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
