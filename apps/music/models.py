from django.db.models import *

class Music(Model):
    name = CharField(max_length=256)
    about = TextField(blank=True)
    released_date = DateField(auto_now=True)
    def __str__(self):
        return f"{self.name}"