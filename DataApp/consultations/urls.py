from django.urls import path
from .views import ConsultationListView, ConsultationCreateView, ConsultationRetrieveUpdateDestroyView

urlpatterns = [
    path('consultations/', ConsultationListView.as_view(), name='Consultation-list'),
    path('consultations/create/', ConsultationCreateView.as_view(), name='Consultation-create'),
    path('consultations/<int:pk>/', ConsultationRetrieveUpdateDestroyView.as_view(), name='Consultation-detail'),
]