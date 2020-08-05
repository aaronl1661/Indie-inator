from django.db import models


class IP(models.Model):
    ip = models.CharField(max_length=40)

