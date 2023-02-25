from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department
from datetime import datetime

# Create your views here.


def index(request):
    return render(request, 'index.html')


def all_emp(request):
    # Grab all the Data from the model
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'view_all_emp.html', context)


def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        phone = int(request.POST['phone'])
        bonus = int(request.POST['bonus'])
        new_emp = Employee(first_name=first_name,
                           last_name=last_name, salary=salary, dept_id=dept, role_id=role, phone=phone, bonus=bonus, hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('Employee Added')
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse('Something went wrong')


def remove_emp(request):
    return render(request, 'remove_emp.html')


def filter_emp(request):
    return render(request, 'filter_emp.html')
