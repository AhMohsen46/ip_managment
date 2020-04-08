from rest_framework.response import Response
from rest_framework.views import status
from ipaddress import ip_network

def validate_request_data(fn):
    def decorated(*args, **kwargs):
        name = args[0].request.data.get("name", "")
        network_address = args[0].request.data.get("network_address", "")
        if not name or not network_address:
            return Response(
                data={
                    "message": "Both name and network_address are required to create a subnet"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            ip_network(network_address)
            return fn(*args, **kwargs)
        except Exception as e:
            return Response(
                data={
                    "message": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )
    return decorated
