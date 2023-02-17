from django.db import models

# Create your models here.

class Departaments(models.Model):
    DepartmentsId = models.AutoField(primary_key=True)
    DepartmentsName = models.CharField(max_length=200)

class Employees(models.Model):
    EmployeesId = models.AutoField(primary_key=True)
    EmployeesName = models.CharField(max_length=200)
    Departament = models.CharField(max_length=200)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=200)

