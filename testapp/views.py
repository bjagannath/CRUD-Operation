from django.shortcuts import render
from .models import Employee
from .forms import EmployeeForm
# Create your views here.

def retrieve_view(request):
    emp_list = Employee.objects.all()
    return render(request,"testapp/index.html",{"emp_list":emp_list})

def insert_view(request):
    form = EmployeeForm()
    return render(request,"testapp/insert.html",{"form":form})