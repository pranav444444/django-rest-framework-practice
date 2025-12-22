from rest_framework import serializers
from students.models import Student
from employees.models import Employee


    
#Employee Serializer to convert Employee model instances into JSON format and vice versa
class EmployeeSerializer(serializers.ModelSerializer):
  class Meta: #Meta class is used to specify metadata options for the serializer
    model=Employee
    fields='__all__'