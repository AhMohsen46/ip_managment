from rest_framework import serializers
from .models import Subnets


class SubnetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subnets
        fields = ("id", "name", "network_address")