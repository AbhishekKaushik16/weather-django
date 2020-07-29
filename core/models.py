from django.db import models

# Create your models here.

class Locations(models.Model):
    location = models.CharField(max_length=20)

    def __str__(self):
        return self.location

    class Meta:
        verbose_name_plural = 'cities'
