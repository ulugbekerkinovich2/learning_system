from rest_framework import serializers

from basic_app.models import CustomUser, Marks, Message, Students
from basic_app import models


class UserSerializer1(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = 'id', 'username', 'password', 'is_active', 'is_staff', 'is_superuser', 'first_name', 'last_name', 'email', 'image', 'subject', 'role'

    def create(self, validated_data):
        return models.CustomUser.objects.create_user(**validated_data)


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marks
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"
