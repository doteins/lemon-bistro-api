from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu, Booking

class userSerializer(serializers.ModelSerializer):
	class sMeta:
		model = User
		fields = ['id', 'username', 'email', 'groups', 'url']

class menuSerializer(serializers.ModelSerializer):
	class Meta:
		model = Menu
		fields = '__all__'

class bookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = '__all__'