from django.urls import path
from .views import studentsView, studentDetailView

urlpatterns = [
    path('', studentsView),
    path('<int:pk>/', studentDetailView),
]
