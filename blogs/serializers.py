from rest_framework import serializers
from .models import Blog,Comment

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model=Comment
    fields='__all__'
  
class BlogSerializer(serializers.ModelSerializer):
  comments=CommentSerializer(many=True,read_only=True)  #alwaysremebr whaterver "related_name" you gave in comments in models.py only use that name only here as well
  class Meta:
    model=Blog
    fields='__all__'