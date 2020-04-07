from django.urls import path
from .views import ListSubnetsView


urlpatterns = [
    path('subnets/', ListSubnetsView.as_view(), name="subnets-all")
]