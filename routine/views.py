from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt #decorador csrf para permitir a otros dominios acceder a nuestros metodos API
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from routine.models import Departaments, Employees
from routine.serializers import DepartamentsSerializer, EmployeeSerializer
# Create your views here.

@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        departments = Departaments.objects.all()
        departments_serializer=DepartamentsSerializer(departments,many=True)
        print('recibido')
        return JsonResponse(departments_serializer.data,safe=False)
    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        departments_serializer=DepartamentsSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif  request.method=='PUT':
        department_data=JSONParser().parse(request)
        department = Departaments.objects.get(DepartamentId=department_data['DepartamentId'])
        departament_serializer=DepartamentsSerializer(department,data=department_data)
        if departament_serializer.is_valid():
            departament_serializer.save()
            return JsonResponse("Update Successfully", safe= False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        department=Departaments.objects.get(DepartamentId=id)
        department.delete()
        return JsonResponse("Deleted Successully", safe=False)



