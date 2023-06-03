from django.db import models


class Title(models.Model):
    name = models.CharField(max_length=128)
    pub_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    humans = models.ManyToManyField(
        'Human',
        related_name='titles',
        blank=True,
    )
    places = models.ManyToManyField(
        'Place',
        related_name='titles',
        blank=True,
    )
    image = models.ImageField()


class Human(models.Model):
    name = models.CharField(max_length=128)
    age = models.SmallIntegerField()
    bio = models.TextField()
    image = models.ImageField()


class Place(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    image = models.ImageField()
