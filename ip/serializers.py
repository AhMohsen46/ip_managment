from rest_framework import serializers
from .models import Ips


class IpsSerializer(serializers.ModelSerializer):
    # subnet_id = serializers.CharField(source='subnet_id')

    class Meta:
        model = Ips
        fields = ("id", "ip_address", "subnet_id", "vlan_id")