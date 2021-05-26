from django.db import models


class Show(models.Model):
    title = models.CharField(max_length = 45)
    network = models.CharField(max_length = 45)
    reld = models.TextField(null=True)
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)