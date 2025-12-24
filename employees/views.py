
from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse



from .serializers import  EmployeeSerializer
from rest_framework.response import Response

from rest_framework import status

from rest_framework.decorators import api_view #decorator to specify allowed HTTP methods for a view function

from rest_framework.views import APIView #base class for creating class-based views in DRF
# Create your views here.

from employees.models import Employee

from django.http import Http404

from rest_framework import mixins, generics,viewsets

from employees.filters import EmployeeFilter


from rest_framework.authentication import TokenAuthentication #use this for generating token







# from blogs.models import Blog,Comment

# from blogs.serializers import BlogSerializer,CommentSerializer


# Create your views here.
# # Class-Based Views Approach using GenericAPIView and Mixins

# #Mixins are reusable components that provide specific functionality to class-based views

# class Employees(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer

#     def get(self,request): #handle GET requests to retrieve a list of employees
#         return self.list(request)

#     def post(self,request,): #handle POST requests to create a new employee
#         return self.create(request)
      
#   # View to handle retrieving the details of a specific employee
#   # View to handle updating the details of a specific employee
#   # View to handle deleting a specific employee
  
# class EmployeeDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#   queryset=Employee.objects.all()
#   serializer_class=EmployeeSerializer
  
#   def get(self,request,pk): #handle GET requests to retrieve the details of a specific employee based on the provided primary key (pk)
#     return self.retrieve(request,pk)
  
#   def put(self,request,pk): #handle PUT requests to update the details of a specific employee based on the provided primary key (pk)
#     return self.update(request,pk)
  
#   def delete(self,request,pk):
#     return self.destroy(request,pk)
  

  

#Generics


#ListAPIView provides built-in implementations for handling GET requests to retrieve a list of objects and POST requests to create new objects
# class Employees(generics.ListAPIView,generics.CreateAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
  
  
# class Employees(generics.ListCreateAPIView): #ListCreateAPIView provides built-in implementations for handling GET requests to retrieve a list of objects and POST requests to create new objects
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer

# #ListCreateAPIView provides built-in implementations for handling GET requests to retrieve a list of objects and POST requests to create new objects


# #RetrieveAPIView provides built-in implementation for handling GET requests to retrieve a single object based on its primary key (pk)
# #UpdateAPIView provides built-in implementation for handling PUT requests to update a single object based on its primary key (pk)
# #DestroyAPIView provides built-in implementation for handling DELETE requests to delete a single object based on its primary key (pk)
# '''
# class EmployeeDetail(generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#     lookup_field='pk' #specifies that the primary key (pk) will be used to look up the Employee instance
    
# '''
# #RetrieveUpdateDestroyAPIView combines the functionality of RetrieveAPIView, UpdateAPIView, and DestroyAPIView into a single class

# class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#     lookup_field='pk' #specifies that the primary key (pk) will be used to look up the Employee instance





# ViewSets: 

# class EmployeeViewset(viewsets.ViewSet):
#   def list(self,request):
#     queryset=Employee.objects.all()
#     serializer=EmployeeSerializer(queryset,many=True)
#     return Response(serializer.data)
  
  
#   def create(self,request):
#      serializer=EmployeeSerializer(data=request.data)
#      if serializer.is_valid():
#        serializer.save()
#        return Response(serializer.data,status=status.HTTP_201_CREATED)
#      return Response(serializer.errors)
   
#   def retrieve(self,request,pk=None):
#     employee=get_object_or_404(Employee,pk=pk)
#     serializer=EmployeeSerializer(employee)
#     return Response(serializer.data,status=status.HTTP_200_OK)
  
#   def update(self,request,pk=None):
#     employee=get_object_or_404(Employee,pk=pk)
#     serializer=EmployeeSerializer(employee,data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data)
#     return Response(serializer.errors)
  
#   def delete(self,request,pk=None):
#     employee=get_object_or_404(Employee,pk=pk)
#     employee.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)
  
  


#Model ViewSets:
      
      
   
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filterset_class=EmployeeFilter
    
    #we have already declarfed in settings.py globally 
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

  
  
  