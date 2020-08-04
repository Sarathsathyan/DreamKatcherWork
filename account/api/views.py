from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from django.shortcuts import render,redirect
from django.contrib import messages
from account.models import UserMore
# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def get(self,request):

        return render(request,"accounts/register.html")
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        context={
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1],
            "message":"successfully registered"
        }
        messages.success(request,"Register successfully")

        return render(request,'accounts/login.html',context)
        # return Response({
        # "user": UserSerializer(user, context=self.get_serializer_context()).data,
        # "token": AuthToken.objects.create(user)[1]
        # })
from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    def get(self,request):

        return render(request,"accounts/login.html")

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        try:

            login(request, user)
            if request.user.is_active:
                context ={
                    "first_name":user.first_name,
                    "last_name":user.last_name,
                    "email":user.email,
                    "username":user.username
                }
                return render(request,"accounts/dash.html",context)
        except:
            print("error")
        return super(LoginAPI, self).post(request, format=None)