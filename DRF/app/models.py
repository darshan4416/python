from django.db import models

class student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=12)
    fname = models.CharField(max_length=20)

    def __str__(self):
        return self.name
