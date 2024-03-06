from django.contrib.admin import *
from .models import Album

@register(Album)
class AlbumAdmin(ModelAdmin):
    list_display = ("id", "name")

