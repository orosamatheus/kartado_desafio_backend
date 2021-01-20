from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=50)
    color_hex = models.CharField(max_length=7)


class Road(models.Model):
    name = models.CharField(max_length=50)
    uf_code = models.CharField(max_length=2)
    length = models.FloatField()


class Occurrence(models.Model):
    description = models.CharField(max_length=50)
    road = models.ForeignKey(
        "occurrences.Road", null=True, on_delete=models.SET_NULL
    )
    km = models.CharField(max_length=50)
    status = models.ForeignKey(
        "occurrences.Status", null=True, on_delete=models.SET_NULL
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
