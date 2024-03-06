
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("rest_framework.urls")),
    path("api/model/", include("apps.album.urls")),
    path("api/model/", include("apps.artist.urls")),
    path("api/model", include("apps.music.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
