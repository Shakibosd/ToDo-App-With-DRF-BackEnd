from django.db import models

class Plan(models.Model):
    title = models.CharField(max_length=200)
    product = models.IntegerField()