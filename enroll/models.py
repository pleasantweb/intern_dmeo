from django.db import models

# Create your models here.

class KeyValue(models.Model):
    key = models.CharField(max_length=1)
    value = models.IntegerField()

    def __str__(self):
        return self.key