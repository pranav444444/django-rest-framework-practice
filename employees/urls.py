from rest_framework.routers import DefaultRouter

from .views import EmployeeViewSet
#🔹 Built-in DRF View for Token Generation
# DRF provides:
# obtain_auth_token
# This view:
# •	Validates username & password
# •	Creates token if not present
# •	Returns token as JSON



from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('employees', EmployeeViewSet, basename='employee')


# urlpatterns = [
    
#     router.urls
# ]

urlpatterns = [
    path('', include(router.urls)),
    
]

# path('employees/',views.Employees.as_view()), #Class based view for Employee list and create
    # #in views.py Employees is a class so we need to call as_view() method to convert the class into a view function that can be used in URL patterns
    # path('employees/<int:pk>/',views.EmployeeDetail.as_view()), #Class based view for Employee retrieve, update, delete
    # #In views.py EmployeeDetail is a class so we need to call as_view() method to convert the class into a view