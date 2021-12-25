from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(allow_null=True)

    class Meta:
        model = User
        fields = '__all__'
