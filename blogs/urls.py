from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter  




urlpatterns = [
    # path('students/',views.studentsView),
    # path('students/<int:pk>/',views.studentDetailView), #pk is primary key
    
    # path('employees/',views.Employees.as_view()), #Class based view for Employee list and create
    # #in views.py Employees is a class so we need to call as_view() method to convert the class into a view function that can be used in URL patterns
    # path('employees/<int:pk>/',views.EmployeeDetail.as_view()), #Class based view for Employee retrieve, update, delete
    # #In views.py EmployeeDetail is a class so we need to call as_view() method to convert the class into a view
    # path('',include(router.urls)),
    
    
    path('blogs/',views.BlogsView.as_view()),
    path('comments/',views.CommentsView.as_view()),
    

    #for primary key based operation in blogs-comment model
    path('blogs/<int:pk>/',views.BlogDetailView.as_view()),
    path('comments/<int:pk>/',views.CommentDetailView.as_view())
]