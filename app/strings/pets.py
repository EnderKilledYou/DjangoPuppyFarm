from django.db import models
from factory import Faker
from factory.django import DjangoModelFactory
from rest_framework.serializers import ModelSerializer


class Pet(models.Model):
    app_label="strings"
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

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
