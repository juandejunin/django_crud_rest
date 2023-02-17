from rest_framework import serializers
from routine.models import Employees, Departaments

class DepartamentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departaments
        fields=('DepartmentsId','DepartmentsName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields=('EmployeeId','EmployeeName','Departament','DateOfJoing','PhotoFileName')