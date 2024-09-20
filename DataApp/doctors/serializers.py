from .models import Doctor
from rest_framework import serializers

class DoctorSerializer(serializers.ModelSerializer):
    specialization_name = serializers.CharField(source='specialization.name', read_only=True)
    
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialization', 'specialization_name', 'email', 'phone', 'address']
    
