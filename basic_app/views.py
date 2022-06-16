from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

# Create your views here.
from rest_framework.response import Response

from basic_app import serializers, models
from basic_app.models import CustomUser, Message, Marks, Students


def index(request):
    return HttpResponse('Application will be working')


class ListUser(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = serializers.UserSerializer


class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = serializers.UserSerializer


class ListMessage(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = serializers.MessageSerializer


class DetailMessage(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = serializers.MessageSerializer


class ListMarks(generics.ListCreateAPIView):
    queryset = Marks.objects.all()
    serializer_class = serializers.MarkSerializer


class DetailMarks(generics.RetrieveUpdateDestroyAPIView):
    queryset = Marks.objects.all()
    serializer_class = serializers.MarkSerializer


class ListStudent(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = serializers.StudentSerializer


class DetailStudent(generics.RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = serializers.StudentSerializer


from rest_framework_simplejwt.tokens import RefreshToken


class GetCustomToken(generics.GenericAPIView):
    serializer_class = serializers.UserSerializer1
    queryset = models.CustomUser.objects.all()

    def post(self, request, *args, **kwargs):
        admin = self.serializer_class(data=request.data)

        if admin.is_valid():
            print(admin.validated_data)
            try:
                user = authenticate(username=admin.validated_data['username'],
                                    password=admin.validated_data['password'])
                print(user.is_active, user.is_staff, user.is_superuser, user.username, user.password)

                if user:
                    refresh = RefreshToken.for_user(user)
                    return Response({
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                        'role': str(user.role),
                        'id': str(user.id)

                    })

            except Exception as e:
                print(e)
            return Response({'detail': 'User topilmadi, qaytadan urinib ko\'ring'})
        return Response(admin.errors)
