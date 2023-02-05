from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *


@admin.register(Key)
class StringsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
