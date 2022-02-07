from dataclasses import fields
from rest_framework import serializers
from django.db.models import Avg
from .models import Car , Rate


class RateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rate
		fields = '__all__'


class CarListSerializer(serializers.ModelSerializer):
	avg_rating = serializers.SerializerMethodField()
	class Meta:
		model = Car
		fields = '__all__'

	def get_avg_rating(self , obj):
		value =	obj.rates.aggregate(Avg('value'))
		return value['value__avg']


class CarSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Car
		fields = '__all__'


class PopularSerializer(serializers.ModelSerializer):
	rates_number = serializers.IntegerField()
	class Meta:
		model = Car
		fields = '__all__'
