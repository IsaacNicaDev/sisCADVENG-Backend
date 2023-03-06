from django.db import models
from catalogs.models import *

# Create your models here.

class Student(models.Model):
    student_code = models.CharField(max_length=30, unique=True)
    picture = models.ImageField(null=True, upload_to='foto')
    first_name = models.CharField(max_length=15)
    second_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    second_lastname = models.CharField(max_length=15)
    location_id = models.ForeignKey()
    date_birth = models.DateField()
    nationality_id = models.ForeignKey()
    address = models.CharField(max_length=50)
    religion_id = models.ForeignKey(Religion, on_delete=models.CASCADE)
    native_language_id = models.ForeignKey(Language, on_delete=models.CASCADE)
    disability_id = models.ForeignKey(Disability, on_delete=models.CASCADE)
    birth_certificate = models.BooleanField(unique=True)
    tutor_id = models.ForeignKey( on_delete=models.CASCADE)
    gender_id = models.ForeignKey(Gender, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

class Professor(models.Model):
    first_name = models.CharField(max_length=15)
    second_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    second_lastname = models.CharField(max_length=15)
    age = models.IntegerField()
    marital_status = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    number_children = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
class Location(models.Model):
    country_id = models.ForeignKey(Country)
    city_id = models.ForeignKey(City)
    departament_id = models.ForeignKey(Departament)
    zone_id = models.ForeignKey(Zone)
    district_id = models.ForeignKey(District)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

class Tutor(models.Model):
    first_name = models.CharField(max_length=15)
    second_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    second_lastname = models.CharField(max_length=15)
    id_number = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    consanguinity = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
class Enrollment(models.Model):
    student_id = models.ForeignKey(Student)
    group_id = models.ForeignKey()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

class Group(models.Model):
    grade_id = models.ForeignKey(Grade)
    academic_year = models.IntegerField()
    guide_professor_id = models.ForeignKey(Professor)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

class Marking(models.Model):
    subject_id = models.ForeignKey(Subject)
    professor_id = models.ForeignKey(Professor)
    student_id = models.ForeignKey(Student)
    marking = models.IntegerField()
    evaluation_cutoff = models.ForeignKey()
    grade_id = models.ForeignKey(Grade)
    group_id = models.ForeignKey(Group)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)