from rest_framework.viewsets import ModelViewSet

from .models import Artist
from .serializers import ArtistSerializer
import logging

logger = logging.getLogger("main")
class ArtistViewSet(ModelViewSet):
    logger.info("artist")
    queryset=Artist.objects.all()
    serializer_class=ArtistSerializer
