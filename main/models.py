from django.db import models
import uuid

# Create your models here.

class Tag(models.Model):

    name = models.CharField(max_length = 40)

    def __str__(self): 

        return self.name
    

class Ingredient(models.Model):
    name = models.CharField(max_length = 40)
    quantity = models.CharField(max_length = 40)

    def __str__(self):

        return self.name


class Recipe(models.Model):

    name = models.CharField(max_length = 400)
    details = models.CharField(max_length=500)
    ingredients = models.ManyToManyField(Ingredient)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name