from rest_framework import serializers
from places.models import Place

class PlaceSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    description = serializers.CharField(required=False)

    def create(self, validated_data):
        place = Place(**validated_data).save()
        return place
