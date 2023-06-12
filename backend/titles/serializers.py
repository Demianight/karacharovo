from rest_framework import serializers
from .models import Title, Place, Human


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '*'


class HumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = '*'


class TitleSerializer(serializers.ModelSerializer):
    humans = HumanSerializer(many=True)
    places = PlaceSerializer(many=True)

    class Meta:
        model = Title
        fields = '*'
