from django.urls import path
from .views import ListSubnetsView, SubnetsDetailView


urlpatterns = [
    path('', ListSubnetsView.as_view(), name="subnets-list-create"),
    path('<int:pk>', SubnetsDetailView.as_view(), name="subnets-detail"),

]