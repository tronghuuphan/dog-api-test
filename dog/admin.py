from django.contrib import admin
from .models import Dog, Breed

# Register your models here.
@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'breed', 'gender', 'color')
    search_fields = ('name',)

@admin.register(Breed)
class Breed(admin.ModelAdmin):
    list_display = ('name', 'size')