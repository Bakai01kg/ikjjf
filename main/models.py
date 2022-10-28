from contextlib import nullcontext
from enum import unique
from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin, AbstractUser
from django.forms import EmailField

class UserManager(BaseUserManager):
    def _create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError('вы не ввели email')
        user= self.model(
            email = self.normalize_email(email),
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,email,password):
        return self._create_user(email,password)

    def create_superuser(self,email,password):
        return self._create_user(email,password,is_staff = True,is_superuser = True)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50, unique=True)  # 
    surname = models.CharField(max_length = 50,unique = True)
    email = models.EmailField(max_length=100, unique=True)  # Email
    is_active = models.BooleanField(default=True)  # Статус активации
    is_staff = models.BooleanField(default=False)  # Статус админа
    GENDER = [
    ('male','male'),
    ('female','female')]
    gender = models.CharField(max_length=255, choices=GENDER, default='male', null=True)
    birth_date = models.DateField(null = True)
    USERNAME_FIELD = 'email'  # Идентификатор для обращения
    REQUIRED_FIELDS = []  # Список имён полей для Superuser
    objects = UserManager()  # Добавляем методы класса UserManager
    # Метод для отображения в админ панели
    def __str__(self):
        return self.email










