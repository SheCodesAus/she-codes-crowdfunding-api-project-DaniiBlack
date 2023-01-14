# yellow line is VS code being buggy. It doesn't know we have the venv, and thus thinks we don't have restframework installed 
 
from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.Serializer):
    # on the model, we didn't need to add an id. Django framework knows to add an id and does so automagically.
    # Users do not get to pick an id, for sake of avoiding overlap. Next piece of code generates one. 
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField(read_only=True)
    owner = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Project.objects.create(**validated_data)