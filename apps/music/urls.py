from rest_framework.routers import DefaultRouter

from .views import MusicViewSet

router=DefaultRouter()
router.register('music', MusicViewSet, basename='music')

urlpatterns=[]
urlpatterns+=router.urls