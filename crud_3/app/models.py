from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField()
    marks = models.IntegerField()
    batch = models.CharField()
    branch = models.CharField()

    def __str__(self):
        return self.name
    