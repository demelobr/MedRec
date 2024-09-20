from .models import Doctor
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import DoctorSerializer

class DoctorListView(generics.ListAPIView):
    queryset = Doctor.objects.select_related('specialization').all()
    serializer_class = DoctorSerializer
    permission_classes = [AllowAny]