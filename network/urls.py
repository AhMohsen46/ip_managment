from django.urls import path
from .views import ListSubnetsView, SubnetsDetailView


urlpatterns = [
    path('subnets/', ListSubnetsView.as_view(), name="subnets-list-create"),
    path('subnets/<int:pk>', SubnetsDetailView.as_view(), name="subnets-detail"),

]