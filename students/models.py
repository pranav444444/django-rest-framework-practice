from django.db import models

# Create your models here.
#Here we are creating Student model
#models are used to create database tables
class Student(models.Model):
  #inside the model we are defining fields or columns
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.CharField(max_length=100)

   #string representation of the model
   #It helps to identify the object by its name
    def __str__(self):
        return self.name