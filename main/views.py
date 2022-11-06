from rest_framework import status
from rest_framework.generics import CreateAPIView,ListCreateAPIView,UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from main.models import User,Profile
from main.serializers import UserRegisterSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import ProfileSerializer
from rest_framework import generics
from django.core.mail import EmailMessage
from .utils import Util
import random

k=random.randint(10000,99999)

class UserRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]


    # Создаём метод для создания нового пользователя
    def post(self, request, *args, **kwargs):
        user = request.data
 
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        email = serializer.validated_data['email']
        user = User.objects.get(email=email)
        user.save()
        email_body = 'Привет ' + user.email + '\n код дял подтверждение электронной почты \n' + f'{k}'
        data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Подтвердить электронную почту'}
        Util.send_email(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
            


class ProfileList(ListCreateAPIView):
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ProfileSerializer
    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer






  




