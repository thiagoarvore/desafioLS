from django.db import models
import uuid
from professionals.models import Professional


class Appointment(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    professional = models.ForeignKey(
        Professional, on_delete=models.CASCADE, null=False, blank=False
    )
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.professional} - {self.date}: {self.time}"
