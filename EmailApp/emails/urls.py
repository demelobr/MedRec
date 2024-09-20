from django.urls import path
from .views import EmailSendView

urlpatterns = [
    path('emails/send/', EmailSendView.as_view(), name='send_email'),
]
