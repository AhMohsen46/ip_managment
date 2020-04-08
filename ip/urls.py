from django.urls import path
from .views import ListIpsView, IpsDetailView


urlpatterns = [
    path('', ListIpsView.as_view(), name="ips-list-create"),
    path('<int:pk>', IpsDetailView.as_view(), name="ips-detail"),
]