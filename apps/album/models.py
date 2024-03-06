from django.db.models import *
from apps.music.models import Music
class Album(Model):
    name = CharField(max_length=64)
    about = TextField(blank=True)
    musics = ManyToManyField(Music)
    released_date = DateField(auto_now=True)

    def __str__(self):
        return f"{self.name}"