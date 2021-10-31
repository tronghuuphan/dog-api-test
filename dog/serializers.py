from rest_framework import serializers
from .models import Dog, Breed

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ('id','name', 'size', 'friendliness', 'trainability', 'dogs_count')
    
    dogs_count = serializers.IntegerField(read_only=True)

class SimpleBreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ('id', 'name', 'size')

class DogSerializer(serializers.ModelSerializer):
    breed = SimpleBreedSerializer(read_only=True)
    class Meta:
        model = Dog
        fields = ('id', 'name', 'age', 'gender', 'breed', 'color', 'favorite_food', 'favorite_toy',)
    
class CreateDogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = '__all__'

