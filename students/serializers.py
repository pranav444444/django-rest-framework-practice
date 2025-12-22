

from rest_framework import serializers
from students.models import Student

#Student Serializer does the job of converting Student model instances into JSON format and vice versa

# class StudentSerializer(serializers.ModelSerializer): #serializers.ModelSerializer is a built-in class in DRF that provides a way to create serializers based on Django models
#   class Meta: #Meta class is used to specify metadata options for the serializer
#     model=Student
#     fields='__all__'
class StudentSerializer(serializers.ModelSerializer): #serializers.ModelSerializer is a built-in class in DRF that provides a way to create serializers based on Django models
  class Meta: #Meta class is used to specify metadata options for the serializer
    model=Student
    fields='__all__'