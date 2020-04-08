from django.db import models
from subnet.models import Subnets

class Ips(models.Model):
    # ip address
    ip_address = models.CharField(max_length=15,unique=True, null=False)
    # subnet id
    subnet_id =  models.ForeignKey(Subnets, on_delete=models.CASCADE)
    # vlan id
    vlan_id = models.IntegerField(null = True)


    def __str__(self):
        return "{} - {} - {}".format(self.ip_address, self.subnet_id, self.vlan_id)