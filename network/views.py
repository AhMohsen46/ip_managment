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