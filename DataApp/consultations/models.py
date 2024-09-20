from django.db import models
from doctors.models import Doctor
from django.contrib.auth.models import User

class Consultation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Consultation with Dr. {self.doctor.name} for {self.patient} on {self.date} at {self.time}"
