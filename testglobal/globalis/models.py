# Create your models here.
from django.db import models


class Professor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=18)

    def __str__(self):
        return f'Professor ({self.id}): {self.first_name} | {self.last_name} | {self.age}'

class Subject(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'Subject ({self.id}): {self.name}'


class Textbook(models.Model):
    title = models.CharField(max_length=30)
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Professor)

    def __str__(self):
        return f'Textbook ({self.id}): {self.title} | {self.subject}'