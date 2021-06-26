"""oowlish_test URL Configuration

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
from django.conf.urls import url
from api.views import CustomersViewSet
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title = 'Some cool text')
router = routers.DefaultRouter()
router.register('customer', CustomersViewSet, basename = 'Customers')

urlpatterns = [
    url('doc/', schema_view, name = 'swagger'),
    path('admin/', admin.site.urls),
    path('', include(router.urls))

]
