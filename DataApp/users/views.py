from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer

# View para listar usuários (autenticação necessária)
class UserListView(generics.ListAPIView):
    queryset = User.objects.all().filter(is_superuser=False)
    serializer_class = UserSerializer
    #permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

# View para criar novos usuários (sem autenticação necessária)
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

# Recuperar, atualizar e deletar um usuário específico
class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]