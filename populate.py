import os, django
from faker import Faker
from random import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fbvcrudproject.settings')
django.setup()

from testapp.models import Employee

faker = Faker()
def populate(n):
    for i in range(n):
        feno=randint(1001,9999)
        fename=faker.name()
        fesal=randint(10000,20000)
        feaddr=faker.city()
        emp_records=Employee.objects.get_or_create(
            eno=feno,
            ename=fename,
            esal=fesal,
            eaddr=feaddr)
n=int(input("Enter no. of employees: "))
populate(n)
print(f'{n} records inserted successfully...')