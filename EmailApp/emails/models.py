from django.db import models

class Email(models.Model):
    to_address = models.EmailField()  # Endereço de e-mail do destinatário
    subject = models.CharField(max_length=255)  # Assunto do e-mail
    body = models.TextField()  # Corpo do e-mail
    sent_at = models.DateTimeField(auto_now_add=True)  # Data e hora em que o e-mail foi enviado

    def __str__(self):
        return f"Email to {self.to_address} with subject: {self.subject}"
