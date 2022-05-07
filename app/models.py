from django.db import models

# Create your models here.
class Student(models.Model):
    title=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    roll=models.IntegerField()

    def __str__(self):
        return self.name

