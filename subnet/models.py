from django.db import models


class Subnets(models.Model):
    # subnet name
    name = models.CharField(max_length=255, null=False)
    # network address
    network_address = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.name, self.network_address)