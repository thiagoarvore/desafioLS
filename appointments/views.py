from rest_framework import generics
from .models import Appointment
from .serializers import AppointmentSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from professionals.models import Professional


class AppointmentListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )
    queryset = Appointment.objects.prefetch_related('professional')
    serializer_class = AppointmentSerializer

class ProfessionalAppointmentListAPIView(generics.ListAPIView):
    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )
    queryset = Appointment.objects.prefetch_related('professional')
    serializer_class = AppointmentSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        prof_id = self.kwargs['pk']
        qs = super().get_queryset()
        return qs.filter(professional=prof_id)


class UserAppointmentListAPIView(generics.ListAPIView):
    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )
    queryset = Appointment.objects.prefetch_related('professional')
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        professional = Professional.objects.get(user=self.request.user)
        qs = super().get_queryset()
        return qs.filter(professional=professional)

class AppointmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
