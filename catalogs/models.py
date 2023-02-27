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
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Municipality(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Educationallevel(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Modality(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Turn(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Educationalinstitution(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Typeofincome(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name