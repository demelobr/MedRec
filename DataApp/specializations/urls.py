from django.urls import path
from .views import SpecializationListView

urlpatterns = [
    path('specializations/', SpecializationListView.as_view(), name='specialization-list'),
]