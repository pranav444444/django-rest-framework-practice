from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse

from students.views import students

from students.models import Student

from .serializers import StudentSerializer, EmployeeSerializer
from rest_framework.response import Response

from rest_framework import status

from rest_framework.decorators import api_view #decorator to specify allowed HTTP methods for a view function

from rest_framework.views import APIView #base class for creating class-based views in DRF
# Create your views here.

from employees.models import Employee

from django.http import Http404

from rest_framework import mixins, generics,viewsets

from blogs.models import Blog,Comment

from blogs.serializers import BlogSerializer,CommentSerializer

from .paginations import CustomPagination

@api_view(['GET','POST']) #this view only allows GET requests, POST requests
def studentsView(request):
  if request.method=='GET':#get all the data from Student model and return as JSON response
    students=Student.objects.all()
    serializer=StudentSerializer(students,many=True) #many=True indicates that we are serializing a queryset containing multiple Student instances
    return Response(serializer.data,status=status.HTTP_200_OK) #status.HTTP_200_OK indicates that the request was successful and the server is returning the requested data
  elif request.method=='POST': #create a new student record in the database
    serializer=StudentSerializer(data=request.data) #request.data contains the incoming data from the client that we want to deserialize and validate
    if serializer.is_valid(): #check if the incoming data is valid according to the serializer's validation rules
      serializer.save() #save the new Student instance to the database
      return Response(serializer.data,status=status.HTTP_201_CREATED) #status.HTTP_201_CREATED indicates that a new resource has been successfully created
    print(serializer.errors)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) #if the data is not valid return the validation errors with status code 400 Bad Request

    
    
    
    #Alternative Manual Serialization Approach
  
  
  #fetch all student data from Student model
    # students=Student.objects.all()
    # students=list(students.values())#convert queryset to list of dicts manual serialization
    # return JsonResponse(students,safe=False) #safe=False allows us to return non-dict objects like lists as by default JsonResponse only accepts dict objectss
  
  #Manual Serialization: Converting complex data types like querysets to native Python data types like lists and dicts that can then be easily rendered into JSON format
  
  
@api_view(['GET','PUT','DELETE'])#this view allows GET and PUT requests and DELETE requests
  
def studentDetailView(request,pk):
    try:
      student=Student.objects.get(pk=pk) #fetch a single Student instance based on the provided primary key (pk)
    except Student.DoesNotExist:
      return Response({'error':'Student not found'},status=status.HTTP_404_NOT_FOUND) #if the Student with the given pk does not exist return 404 Not Found response
    
    if request.method=='GET': #retrieve the details of the specified student
      serializer=StudentSerializer(student) #serialize the Student instance
      return Response(serializer.data,status=status.HTTP_200_OK) #return the serialized data with status code 200 OK
    elif request.method=='PUT': #update the details of the specified student
      serializer=StudentSerializer(student,data=request.data) #deserialize the incoming data and update the existing Student instance
      if serializer.is_valid(): #check if the incoming data is valid
        serializer.save() #save the updated Student instance to the database
        return Response(serializer.data,status=status.HTTP_200_OK) #return the updated serialized data with status code 200 OK
      else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) #if the data is not valid return the validation errors with status code 400 Bad Request
      
    elif request.method=='DELETE': #delete the specified student
        student.delete() #delete the Student instance from the database
        return Response(status=status.HTTP_204_NO_CONTENT) #return status code 204 No Content indicating that the deletion was successful but there is no content to return
      
      
      
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
      
   
class EmployeeViewset(viewsets.ModelViewSet):
  queryset=Employee.objects.all()
  serializer_class=EmployeeSerializer
  pagination_class=CustomPagination
  
  
# Blog View

class BlogsView(generics.ListCreateAPIView):
  queryset=Blog.objects.all()
  serializer_class=BlogSerializer
  
class CommentsView(generics.ListCreateAPIView):
  queryset=Comment.objects.all()
  serializer_class=CommentSerializer
      
#primiary key based oprations class base views

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset=Blog.objects.all()
  serializer_class=BlogSerializer
  lookup_field='pk'
  

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field='pk'