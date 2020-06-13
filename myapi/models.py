from django.db import models

# Create your models here.
# models.py
from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=60)
    starting_date = models.DateField()
    ending_date = models.DateField()

    def __str__(self):
        return self.name
