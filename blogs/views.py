from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse

# from students.views import students

# from students.models import Student

# from .serializers import StudentSerializer, EmployeeSerializer
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

from rest_framework.filters import SearchFilter,OrderingFilter


# Create your views here.



  
  
# Blog View

class BlogsView(generics.ListCreateAPIView):
  queryset=Blog.objects.all()
  serializer_class=BlogSerializer
  filter_backends=[SearchFilter,OrderingFilter] #we cal slo use here [DjangoFilterBackend] along with [SearchFilter]
  search_fields=['blog_title','blog_body'] #add blog model fields here
  ordering_fields=['id']
  
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