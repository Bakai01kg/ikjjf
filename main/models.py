from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

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
    name = models.CharField(max_length=50)  # 
    surname = models.CharField(max_length = 50)
    email = models.EmailField(max_length=100, unique=True) 
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

class Country(models.Model):
    name=models.CharField(verbose_name='название страны',max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Страна'
        verbose_name_plural='Список стран'

class Club(models.Model):
    name = models.CharField(verbose_name='название клуба', max_length=255)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Клуб'
        verbose_name_plural = 'Список клубов'
  

class Profile(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length = 255)
    birthday = models.DateField()
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),)
    gender = models.CharField(max_length=10, choices=GENDER)
    club = models.ForeignKey(Club,on_delete=models.CASCADE)
    country = models.ForeignKey(Country,on_delete=models.CASCADE,null=True,blank=True,default=1)
    image = models.ImageField(upload_to='img')
    phone = models.CharField(max_length=50)
    def __unicode__(self):
        return u'Profile of user: {0}'.format(self.user.email)


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        post_save.connect(create_profile, sender=User)


def delete_user(sender, instance=None, **kwargs):
    try:
        instance.user
    except User.DoesNotExist:
        pass
    else:
        instance.user.delete()
        post_delete.connect(delete_user, sender=Profile)












