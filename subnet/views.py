from rest_framework import generics
from .models import Subnets
from .serializers import SubnetsSerializer
from rest_framework.response import Response
from rest_framework.views import status
from .decorators import validate_request_data

class ListSubnetsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Subnets.objects.all()
    serializer_class = SubnetsSerializer

    @validate_request_data
    def post(self, request, *args, **kwargs):
        a_subnet = Subnets.objects.create(
            name=request.data["name"],
            network_address=request.data["network_address"]
        )
        return Response(
            data=SubnetsSerializer(a_subnet).data,
            status=status.HTTP_201_CREATED
        )

class SubnetsDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET subnets/:id
    DELETE subnets/:id
    """
    queryset = Subnets.objects.all()
    serializer_class = SubnetsSerializer
    def get(self, request, *args, **kwargs):
        try:
            a_subnet = self.queryset.get(pk=kwargs["pk"])
            return Response(SubnetsSerializer(a_subnet).data)
        except Subnets.DoesNotExist:
            return Response(
                data={
                    "message": "Subnet with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_subnet = self.queryset.get(id=kwargs["pk"])
            a_subnet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Subnets.DoesNotExist:
            return Response(
                data={
                    "message": "Subnet with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

