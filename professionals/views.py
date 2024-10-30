from rest_framework import generics
from .models import Professional
from .serializers import ProfessionalSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission


class ProfessionalListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer


class ProfessionalRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer
