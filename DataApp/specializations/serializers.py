from .models import Specialization
from rest_framework import serializers

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ['name']
