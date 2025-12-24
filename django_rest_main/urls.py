"""
URL configuration for django_rest_main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi 
from rest_framework.authtoken.views import obtain_auth_token


schema_view = get_schema_view(
   openapi.Info(
      title="Django REST Practice API",
      default_version='v1',
      description="APIs for Students, Employees, Blogs & Comments",
      contact=openapi.Contact(email="pranav@example.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('api/v1/gettoken/',obtain_auth_token),
    path("admin/", admin.site.urls),
    #Web Application Endpoint
    # path('students/', include('students.urls')) ,
    # #when we write students/ it will go to students app and check for urls.py file
    
    
    # #API Endpoint
    # path('api/v1/', include('api.urls'))
    #when we write api/v1/ it will go to api app and check for urls.py file
    
    path('api/v1/students/', include('students.urls')),
    path('api/v1/', include('employees.urls')),
    path('api/v1/', include('blogs.urls')),
    
    # Swagger URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
    
]
