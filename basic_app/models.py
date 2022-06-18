from django.db import models

# Create your models here.
from django.utils import timezone

from django.utils.translation import gettext as _

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, username, **extra_fields):

        if not username:
            raise ValueError(_('The name must be set'))

        user = self.model(username=username, **extra_fields)
        user.set_password(extra_fields['password'])
        user.save()
        return user

    def create_superuser(self, username, **extra_fields):

        extra_fields.setdefault('is_staff', True)

        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_active') is not True:
            raise ValueError(_('Superuser must have is_active=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username=username, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    username = models.CharField(_('username'), max_length=50, unique=True)
    role = models.CharField(max_length=20, default="none")
    subject = models.CharField(default='english', max_length=20)
    image = models.ImageField(upload_to='images/')
    email = models.EmailField(max_length=30)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()


def __str__(self):
    return f'{self.username}'


class Students(models.Model):
    name = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="name1")
    file = models.FileField(upload_to='files/')
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    subject = models.CharField(default='english', max_length=20)

    def __str__(self):
        return self.file


class Marks(models.Model):
    student_name = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='student_names')
    max_mark = models.IntegerField(default='100')
    student_mark = models.IntegerField()
    subject = models.CharField(default='english', max_length=20)

    def __str__(self):
        return self.subject


class Message(models.Model):
    chat_for_students = models.TextField()

    def __str__(self):
        return self.chat_for_students
