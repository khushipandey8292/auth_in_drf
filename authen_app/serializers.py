from rest_framework import serializers
from .models import Student
# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Student
#         fields=['id','name','roll','city']

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Student
        fields=['id','name','url','roll','city']