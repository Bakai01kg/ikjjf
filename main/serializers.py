from rest_framework import serializers
from main.models import User,Profile

class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()
    class Meta:
        model = User
        fields = ['name','surname','birth_date','gender', 'email', 'password', 'password2']

    def save(self, *args, **kwargs):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        email=self.validated_data['email'],
        if password != password2:
            raise serializers.ValidationError({password: 'пароль не совпадает'})
        user = User(
            name = self.validated_data['name'],
            surname=self.validated_data['surname'],
            email=self.validated_data['email'])
        user.set_password(password)
        user.save()
        return User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'name', 'surname', 'birthday','gender','club','country','image','phone')
        
