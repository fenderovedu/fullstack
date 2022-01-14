from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import json

class AuthView(generics.GenericAPIView):
    def post(self, request):
        data = json.loads(request.body)
        userName = data['username']
        userPass = data['password']
        userMail = data['email']
        user = User.objects.create_user(username=userName,email=userMail,password=userPass)
        if(user):
            content = {'message': 'successfully created user'}
            return Response(content)

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'username': {request.user.username}}
        return Response(content)