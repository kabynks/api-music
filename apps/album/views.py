from rest_framework.viewsets import ModelViewSet

from .models import Album
from .serializers import AlbumSerializer
import logging

logger = logging.getLogger("main")
class AlbumViewSet(ModelViewSet):
    logger.info("Album")
    queryset=Album.objects.all()
    serializer_class=AlbumSerializer
