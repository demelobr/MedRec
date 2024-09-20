from django.core.mail import send_mail
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from EmailApp.settings import EMAIL_HOST_USER
from .models import Email
from .serializers import EmailSerializer

class EmailSendView(generics.CreateAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email_instance = serializer.save()  # Salva o e-mail no banco de dados

        # Enviar o e-mail usando o Django
        try:
            send_mail(
                email_instance.subject,
                email_instance.body,
                EMAIL_HOST_USER,  # O remetente
                [email_instance.to_address],  # Lista de destinatários
                fail_silently=False,
            )
        except Exception as e:
            return Response({"detail": f"E-mail não enviado: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
