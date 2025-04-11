from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
    # django-filter********************************************************
    
    # filter_backends=[DjangoFilterBackend]
    # filterset_fields=['city']
    
    #inherit method by listapiview and apply filter**********************************
    
    # def get_queryset(self):
    #     user=self.request.user
    #     return Student.objects.filter(passby=user)
    
    #search filter*************************************************
    # filter_backends=[SearchFilter]
    # search_fields=['^name'] 
    # search_fields=['=name']
    # search_fields=['city','name']
    
    #order filter*******************************************
    filter_backends=[OrderingFilter]
    Ordering_fields=['name']