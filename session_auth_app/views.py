from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from session_auth_app.throttling import TestRateThrottle
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[SessionAuthentication]
    # permission_classes=[IsAuthenticated]
    # permission_classes=[IsAdminUser]
    # permission_classes=[AllowAny]
    permission_classes=[IsAuthenticatedOrReadOnly]
    # permission_classes=[DjangoModelPermissions]
    # permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
    # throttle_classes=[AnonRateThrottle,UserRateThrottle]
    throttle_classes=[AnonRateThrottle,TestRateThrottle]