from rest_framework import serializers

from .models import (
    HardwareInfo,
    HardwareSession,
    SessionImage
)


class HardwareInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HardwareInfo
        fields = '__all__'
        lookup_field = 'id'


class HardwareSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HardwareSession
        fields = '__all__'
        depth = 3
        lookup_field = 'id'


class SessionImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionImage
        fields = '__all__'
        lookup_field = 'id'