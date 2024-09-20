from .models import Consultation
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import ConsultationSerializer

class ConsultationListView(generics.ListAPIView):
    serializer_class = ConsultationSerializer
    #permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user
        return Consultation.objects.filter(patient=user)

#class ConsultationCreateView(generics.CreateAPIView):
#    queryset = Consultation.objects.all()
#    serializer_class = ConsultationSerializer
#    #permission_classes = [IsAuthenticated]
#    permission_classes = [AllowAny]

import requests
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Consultation
from .serializers import ConsultationSerializer

class ConsultationCreateView(generics.CreateAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Dados da consulta criada
        consultation = serializer.instance
        doctor_name = consultation.doctor.name
        patient_email = consultation.patient.email  # Obtém o e-mail do paciente
        patient_name = consultation.patient.first_name  # Ou use outro campo, se preferir
        consultation_date = str(consultation.date)
        consultation_time = str(consultation.time)

        # Formatar o JSON para enviar para a API de e-mail
        email_data = {
            "to_address": patient_email,  # Usando o e-mail do paciente
            "subject": "Confirmação de Consulta",
            "body": f"Olá {patient_name},\n\nSua consulta com Dr. {doctor_name} foi marcada para {consultation_date} às {consultation_time}.\n\nAtenciosamente,\nMedRec"
        }

        # Enviar requisição para a API de envio de e-mails
        email_response = requests.post("http://127.0.0.1:8002/api/emails/send/", json=email_data)

        print(email_response.status_code)
        print(email_response)

        # Verificar a resposta da API de e-mail
        if email_response.status_code != 200:
            # Lidar com o erro de envio de e-mail se necessário
            return Response({"detail": "Consulta criada, mas falha ao enviar e-mail."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Retornar a resposta da criação da consulta
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ConsultationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    #permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]