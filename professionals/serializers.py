from rest_framework import serializers
from .models import Professional
from accounts.serializers import AccountSerializer
from accounts.models import User


class ProfessionalSerializer(serializers.ModelSerializer):
    user = AccountSerializer()

    class Meta:
        model = Professional
        fields = "__all__"

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = User.objects.create(**user_data)
        professional = Professional.objects.create(user=user, **validated_data)
        return professional

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", None)
        if user_data:
            user_serializer = AccountSerializer(instance.user, data=user_data)
            if user_serializer.is_valid():
                user_serializer.save()
