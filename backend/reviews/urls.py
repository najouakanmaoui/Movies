from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActorViewSet, MovieViewSet, ReviewViewSet

__author__ = 'najouakaanmaoui@gmail.com'

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'actors', ActorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]
