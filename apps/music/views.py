from rest_framework.viewsets import ModelViewSet
import logging
from .models import Music
from .serializers import MusicSerializer

logger = logging.getLogger("main")

class MusicViewSet(ModelViewSet):
    logger.info("music")
    queryset=Music.objects.all()
    serializer_class=MusicSerializer