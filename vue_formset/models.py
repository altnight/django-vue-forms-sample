from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=10)
    is_active = models.BooleanField()
    birthday = models.DateTimeField()
