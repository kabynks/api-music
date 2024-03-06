from django.db.models import *
from apps.album.models import Album
from apps.music.models import Music
class Artist(Model):
    fullname = CharField(max_length=128)
    date_of_birth = DateField(auto_now_add=True, verbose_name="Date of birth")
    albums = ManyToManyField(Album)
    songs = ManyToManyField(Music)
    information = TextField(blank=True)

    def __str__(self):
        return f"{self.fullname}"

