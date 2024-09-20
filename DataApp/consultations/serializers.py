from .models import Consultation
from rest_framework import serializers

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = ['doctor', 'patient', 'date', 'time', 'notes']
