# Create your models here.

from django.db import models
from factory import Faker
from factory.django import DjangoModelFactory
from rest_framework.serializers import ModelSerializer




class Key(models.Model):
    name = models.CharField(max_length=255,default='')
    value = models.CharField(max_length=255,default='')
    last_update = models.DateTimeField(default=0)

    # todo: https://github.com/saxix/django-concurrency
    # https://en.wikipedia.org/wiki/Optimistic_concurrency_control
    def __str__(self):
        return self.name



class KeySerializer(ModelSerializer):
    class Meta:
        model = Key
        fields = (
            'id', 'name', 'value', 'last_update'
        )

