from rest_framework import generics
from .models import Ips
from subnet.models import Subnets
from .serializers import IpsSerializer
from rest_framework.response import Response
from rest_framework.views import status
from .decorators import validate_request_data

class ListIpsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Ips.objects.all()
    serializer_class = IpsSerializer
    @validate_request_data
    def post(self, request, *args, **kwargs):
        subnet_queryset = Subnets.objects.all()
        subnet_id=request.data["subnet_id"]
        a_subnet = subnet_queryset.get(pk=subnet_id)

        a_ip = a_subnet.ips_set.create(
            ip_address=request.data["ip_address"],
            vlan_id=request.data["vlan_id"]
        )
        return Response(
            data=IpsSerializer(a_ip).data,
            status=status.HTTP_201_CREATED
        )

class IpsDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET ips/:id
    DELETE ips/:id
    """
    queryset = Ips.objects.all()
    serializer_class = IpsSerializer
    def get(self, request, *args, **kwargs):
        try:
            a_ip = self.queryset.get(pk=kwargs["pk"])
            return Response(IpsSerializer(a_ip).data)
        except Ips.DoesNotExist:
            return Response(
                data={
                    "message": "Ip with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_ip = self.queryset.get(id=kwargs["pk"])
            a_ip.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Ips.DoesNotExist:
            return Response(
                data={
                    "message": "Ip with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

