from .models import Specialization
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import SpecializationSerializer

class SpecializationListView(generics.ListAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    permission_classes = [AllowAny]
