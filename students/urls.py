from django.urls import path
from .import views

urlpatterns = [
    path('',views.students),
]

# when we go to students/ it will call students function in views.py file