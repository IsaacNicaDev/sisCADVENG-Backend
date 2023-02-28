from django.db import models

# Create your models here.


class Sexo(models.Model):
    DESCRIPCION = (
        ("F", "Femenino"),
        ("M", "Masculino"),
    )
    nombre = models.CharField(max_length=10, null=False)
    descripcion = models.CharField(max_length=1, choices=DESCRIPCION)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.nombre

class Grado(models.Model):
    nombre = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.nombre

class Asignatura(models.Model):
    nombre = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    nombre = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.nombre

class NivelEducativo(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.name

class Modalidad(models.Model):
    nombre = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.nombre

class Seccion(models.Model):
    nombre = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.nombre

class Turno(models.Model):
    nombre = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.nombre

class CentroEducativo(models.Model):
    nombre = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.nombre

class TipoIngreso(models.Model):
    nombre = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    nombre = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.nombre

class Pais(models.Model):
    nombre = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.nombre
    
class Idioma(models.Model):
    nombre = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.nombre

class Etnia(models.Model):
    nombre = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.nombre
    
class Discapacidad(models.Model):
    nombre = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.nombre      

class Religion(models.Model):
    nombre = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.nombre      


class Departamento(models.Model):
    nombre = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.nombre      

class DelegacionDepartamental(models.Model):
    nombre = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.nombre
    
class Zona(models.Model):
    nombre = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.nombre

class Barrio(models.Model):
    nombre = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.nombre               