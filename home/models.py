from django.db import models

# Create your models here.

class TestModel(models.Model):
    number = models.DecimalField(max_digits=7, decimal_places=5)

