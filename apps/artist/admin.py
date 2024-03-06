from django.contrib.admin import *
from .models import Artist

@register(Artist)
class ArtistAdmin(ModelAdmin):
    list_display = ("id", "fullname")
