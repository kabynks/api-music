
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("rest_framework.urls")),
    path("api/dj-rest-auth/", include('dj_rest_auth.urls')),
    path("api/model/", include("apps.album.urls")),
    path("api/model/", include("apps.artist.urls")),
    path("api/model/", include("apps.music.urls")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
