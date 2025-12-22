from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def students(request):
    student_data=[
      {'name':'John Doe','age':21,'course':'Computer Science'}
    ]
    return HttpResponse(student_data)
  
# when we go to students/ it will call this function and return Hello Students