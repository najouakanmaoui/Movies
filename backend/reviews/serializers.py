from rest_framework import serializers
from .models import Movie, Review,Actor
from django.db.models import Avg

__author__ = 'najouakaanmaoui@gmail.com'

class MovieSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        result = super().to_representation(instance)
        actors_data = result['actors']
        actors=Actor.objects.filter(id__in=actors_data).all()
        actors_representation = ActorSerializer(actors, many=True).data
        result['actors'] = actors_representation
        movie_id = instance.id
        average_reviews = Review.objects.filter(movie_id=movie_id).aggregate(Avg('grade'))['grade__avg']
        if average_reviews is not None:
            result['average_reviews'] = int(average_reviews)
        else:
            result['average_reviews'] = None
        return result

    class Meta:
        model = Movie
        fields = '__all__'
    

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'
