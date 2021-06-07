from rest_framework import serializers
from .models import * 
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username' , 'password']

    def create(self,validated_data):
        user = User.objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'

    def validate(self,data):
        if data['age'] < 18:
            raise serializers.ValidationError({'error':'Age cannot be less than 18 !'})
        if data['name'] :
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError({'error':'Name cannot contain anything besides string'})
        return data
