from rest_framework.routers import DefaultRouter

from .views import ArtistViewSet

router=DefaultRouter
router.register('album', ArtistViewSet, basename='album')

urlpatterns=[]
urlpatterns+=router.urls