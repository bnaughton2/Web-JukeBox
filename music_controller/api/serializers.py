from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guestCanPause', 'votesToSkip', 'createdAt')

class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('guestCanPause', 'votesToSkip')