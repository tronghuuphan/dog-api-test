from django_filters.rest_framework import FilterSet
from .models import Dog, Breed

class DogFilter(FilterSet):
    class Meta:
        model = Dog
        fields = {
            'gender': ['exact'],
            'breed__size': ['exact'],
            'age': ['gt', 'lt']
        }

class BreedFilter(FilterSet):
    class Meta:
        model = Breed
        fields = {
            'size': ['exact'],
        }
