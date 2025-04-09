"""
URL configuration for authentication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from authen_app import views as v1
from session_auth_app import views as v2
from rest_framework.routers import DefaultRouter
from custom_perm_app import views as v3
from token_auth_app.auth import CustomAuthToken
from token_auth_app import views as v4
from signal_app import views as v5
from custom_auth_app import views as v6
from jwt_auth import views as v7
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
# from rest_framework.authtoken.views import obtain_auth_token
router=DefaultRouter()
# router.register('studentapi',v1.StudentModelViewSet,basename='student')
# router.register('studentapi',v2.StudentModelViewSet,basename='student')
# # router.register('studentapi',v3.StudentModelViewSet,basename='student')
# router.register('studentapi',v4.StudentModelViewSet,basename='student')
# router.register('studentapi',v5.StudentModelViewSet,basename='student')
# router.register('studentapi',v6.StudentModelViewSet,basename='student')
router.register('studentapi',v7.StudentModelViewSet,basename='student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    # path('gottoken/',obtain_auth_token),
    # path('gottoken/',CustomAuthToken.as_view()),
    path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('reftoken/',TokenRefreshView.as_view(),name='refresh_token'),
    path('verify/',TokenVerifyView.as_view(),name='verify_token'),
]
