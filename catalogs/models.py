from django.db import models

# Create your models here.


class Sex(models.Model):
    DESCRIPTION = (
        ("F", "Femenino"),
        ("M", "Maculino"),
    )
    name = models.CharField(max_length=10, null=False)
    description = models.CharField(max_length=1, choices=DESCRIPTION)

    def __str__(self):
        return self.name

class Degree(models.Model):
    name = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.name

class Municipality(models.Model):
    name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.name

class Educationallevel(models.Model):
    name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.name
