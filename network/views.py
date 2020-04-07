from rest_framework import generics
from .models import Subnets
from .serializers import SubnetsSerializer


class ListSubnetsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Subnets.objects.all()
    serializer_class = SubnetsSerializer