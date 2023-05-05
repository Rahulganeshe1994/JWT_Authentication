from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.views import APIView
from .serializer import RegisterSerializer
from rest_framework import status
from rest_framework.response import Response

# Create your views here.


class RegisterAPIView(APIView):
    def post(self,request):
        serilaizer =RegisterSerializer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data ,  status=status.HTTP_201_CREATED)
        else:
            return Response(serilaizer.errors , status=status.HTTP_400_BAD_REQUEST)
    def get(self , request):
        try:
            data = User.objects.all()
            serializer =RegisterSerializer(data , many = True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response(serializer.data , status=status.HTTP_400_BAD_REQUEST)