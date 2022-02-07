from django.db import models
from django.core.validators import MaxValueValidator , MinValueValidator
# Create your models here.

class Car(models.Model):

	class Meta:
		ordering = ['-id']
		unique_together=[['make','model']]
    
	make = models.CharField(max_length=255)
	model = models.CharField(max_length=255)


class Rate(models.Model):
	car = models.ForeignKey(Car,related_name='rates',on_delete=models.CASCADE)
	value = models.FloatField(default=0 , validators=[MinValueValidator(0),MaxValueValidator(5)])


