from django.contrib.admin import *
from .models import Music

@register(Music)
class MusicAdmin(ModelAdmin):
    list_display = ("id", "name")