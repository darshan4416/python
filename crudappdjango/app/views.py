from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Department, Employee


def index(request):
    employees = Employee.objects.all()
    departments = Department.objects.all()

    data = {
        "employees":employees,
        "departments":departments
    }
    
    return render(request,'base.html',data)

def add(request):
    if request.method == 'POST':
        #name, mname, dept
        name = request.POST.get('name')
        manager_name = request.POST.get('mname')
        dept_name = request.POST.get('dept')

        department = Department(dept_name = dept_name)
        department.save()
        employee = Employee(name=name, manager_name= manager_name, dept=department)
        employee.save()

        # print(name, manager_name, dept_name)
        return redirect('index')

def delete(request,id):
    
    Employee.objects.get(pk=id).delete()

    return redirect('index')

def update(request,id):
    if request.method == 'GET':
        employee = Employee.objects.filter(pk=id)
        print(employee.get('name'))


        return HttpResponse("<h2>yes updated</h2>")

    
    

