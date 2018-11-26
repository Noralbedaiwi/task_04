from django.db import models

# Create a model called Restaurant with the following fields:
# name
# description
# opening_time
# closing_time

class Restaurant(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    