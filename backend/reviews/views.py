from rest_framework import viewsets
from .models import Movie, Review,Actor
from .serializers import ActorSerializer, MovieSerializer, ReviewSerializer
from rest_framework.pagination import PageNumberPagination
from .tasks import simulate_processing  

__author__ = 'najouakaanmaoui@gmail.com'

class MoviePagination(PageNumberPagination):
    page_size = 5

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MoviePagination

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        review = serializer.save()
        simulate_processing.delay(review.id) 
        

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer