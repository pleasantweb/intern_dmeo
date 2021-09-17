from django.contrib import admin
from .models import KeyValue
# Register your models here.

@admin.register(KeyValue)
class KeyValueAdmin(admin.ModelAdmin):
    list_display =['id','key','value']
