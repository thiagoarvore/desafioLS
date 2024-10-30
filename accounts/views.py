from rest_framework import generics
from .models import User
from .serializers import AccountSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission


class AccountListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )
    queryset = User.objects.all()
    serializer_class = AccountSerializer


class AccountRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )
    queryset = User.objects.all()
    serializer_class = AccountSerializer
