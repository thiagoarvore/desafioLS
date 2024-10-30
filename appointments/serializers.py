from rest_framework import serializers
from datetime import date
from .models import Appointment
from professionals.serializers import ProfessionalSerializer


class AppointmentSerializer(serializers.ModelSerializer):
    professional = ProfessionalSerializer()

    class Meta:
        model = Appointment
        fields = "__all__"

    def validate_date(self, value):
        if value < date.today():
            raise serializers.ValidationError(
                "A data deve ser igual ou posterior à data atual."
            )
        return value
