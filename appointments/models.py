from django.db import models
import uuid
from professionals.models import Professional


class Appointment(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, null=False, blank=False)
    date = models.DateField()
    time = models.TimeField()
