# Create your models here.

from django.db import models
from factory import Faker
from factory.django import DjangoModelFactory
from rest_framework.serializers import ModelSerializer


class Pet(models.Model):
    name = models.CharField(max_length=255, default='')
    description = models.TextField(blank=True)
    breed = models.CharField(max_length=255, default='')
    sub_breed = models.CharField(max_length=255, default='')
    url = models.CharField(max_length=610, default='')
    image_size = models.IntegerField(default=0)
    image_height = models.IntegerField(default=0)
    image_width = models.IntegerField(default=0)
    image_format = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class PetFactory(DjangoModelFactory):
    name = Faker('name')
    description = Faker('text')

    class Meta:
        model = Pet



class PetSerializer(ModelSerializer):
    class Meta:
        model = Pet
        fields = (
            'id', 'name', 'description',
        )
