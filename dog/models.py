from django.db import models

# Create your models here.

from django.core import validators
from django.db import models

class Breed(models.Model):
    SIZE_TINY = 'T'
    SIZE_SMALL = 'S'
    SIZE_MEDIUM = 'M'
    SIZE_LARGE = 'L'
    SIZE_CHOICES = [
        (SIZE_TINY, 'Tiny'),
        (SIZE_SMALL, 'Small'),
        (SIZE_MEDIUM, 'Medium'),
        (SIZE_LARGE, 'Large'),
    ]

    name = models.CharField(max_length=255)
    size = models.CharField(
        max_length=1, 
        choices=SIZE_CHOICES,
        default=SIZE_TINY
    )
    friendliness = models.PositiveSmallIntegerField(validators=[validators.MinValueValidator(1), validators.MaxValueValidator(5)])
    trainability = models.PositiveSmallIntegerField(validators=[validators.MinValueValidator(1), validators.MaxValueValidator(5)])
    shedding_amount = models.PositiveSmallIntegerField(validators=[validators.MinValueValidator(1), validators.MaxValueValidator(5)])
    exercise_needs = models.PositiveSmallIntegerField(validators=[validators.MinValueValidator(1), validators.MaxValueValidator(5)])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Dog(models.Model):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_CHOICES = [
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
    ]
    name = models.CharField(max_length=255)
    age = models.IntegerField(validators=[validators.MinValueValidator(0)])
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name='dogs')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    color = models.CharField(max_length=255)
    favorite_food = models.CharField(max_length=255)
    favorite_toy = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
    