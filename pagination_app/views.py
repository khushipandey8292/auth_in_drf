from django.shortcuts import render
from .serializers import StudentSerializers
from .models import Student
from rest_framework.generics import ListAPIView
from .mypagination import MypageNumberPagination,MyLimitOffestPagination
class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    # pagination_class=MypageNumberPagination
    pagination_class=MyLimitOffestPagination
     

#functin based-view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

@api_view(['GET'])
def item_list(request):
    items = Student.objects.all().order_by('id') 
    paginator = PageNumberPagination()
    paginator.page_size = 5  # Set page size here or from settings

    result_page = paginator.paginate_queryset(items, request)
    serializer = StudentSerializers(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

