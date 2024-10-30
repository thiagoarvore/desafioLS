from rest_framework import serializers
from datetime import date
from .models import Appointment
from professionals.models import Professional
from professionals.serializers import ProfessionalSerializer


class AppointmentSerializer(serializers.ModelSerializer):
    professional = ProfessionalSerializer(read_only=True)
    professional_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Appointment
        fields = ['professional', 'professional_id', 'date', 'time']

    def create(self, validated_data):
        validated_data['professional'] = Professional.objects.get(id=validated_data.pop('professional_id'))
        return super().create(validated_data)
    
    def validate_date(self, value):
        if value < date.today():
            raise serializers.ValidationError(
                "A data deve ser igual ou posterior à data atual."
            )
        return value
