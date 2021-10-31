from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Dog, Breed
from .serializers import DogSerializer, CreateDogSerializer, BreedSerializer
from .permissions import IsAdminOrReadOnly
from .paginations import DefaultPagination
from . import filters

class BreedViewSet(ModelViewSet):
    queryset = Breed.objects.annotate(dogs_count=Count('dogs')).all()
    serializer_class = BreedSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.BreedFilter


class DogViewSet(ModelViewSet):
    queryset = Dog.objects.all().select_related('breed')
    pagination_class = DefaultPagination
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend, SearchFilter, )
    filterset_class = filters.BreedFilter
    search_fields = ['breed__name']


    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateDogSerializer
        return DogSerializer
