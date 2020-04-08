from rest_framework.response import Response
from rest_framework.views import status
from subnet.models import Subnets
from ipaddress import ip_network, ip_address

def validate_request_data(fn):
    def decorated(*args, **kwargs):
        ip = args[0].request.data.get("ip_address", "")
        subnet_id = args[0].request.data.get("subnet_id", "")
        if not ip or not subnet_id:
            return Response(
                data={
                    "message": "Both ip_address and subnet_id are required to create a subnet"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        queryset = Subnets.objects.all()
        a_subnet = ip_network(queryset.get(pk=subnet_id).network_address)
        try:
            ip_address(ip)
        except Exception as e:
            return Response(
                data={
                    "message": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        if ip_address(ip) in [a_subnet.broadcast_address, a_subnet.network_address]:
            return Response(
                data={
                    "message": "ip address can't be network or broadcast address "
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        if not ip_address(ip) in a_subnet:
            return Response(
                data={
                    "message": "ip address must belong to the subnet"
                },
                status=status.HTTP_400_BAD_REQUEST
            )            
        return fn(*args, **kwargs)

    return decorated
