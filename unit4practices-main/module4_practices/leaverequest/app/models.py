from django.db import models
from django.utils import timezone

# Create your models here.


class LeaveRequest(models.Model):
    date_requested = models.DateField(default=timezone.now,null=True)
    employee_name = models.CharField(max_length=100)
    is_sick = models.BooleanField(default=False)
    is_personal = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    approved_by = models.TextField(max_length=100)
    notes = models.TextField(null=True, blank=True)


def __str__(self):
    return LeaveRequest.employee_name


def create_request(
    date,
    employee,
    sick,
    personal,
    paid,
    is_approved,
    approved,
    notes=None,
):
    request = LeaveRequest.objects.create(
        date_requested=date,
        employee_name=employee,
        is_sick=sick,
        is_personal=personal,
        is_paid=paid,
        is_approved=is_approved,
        approved_by=approved,
        notes=notes,
    )
    request.save()

def approve_request(name):
    employee = LeaveRequest.objects.get(employee_name=name)
    employee.is_approved = True
    employee.save()
    return employee


def search_by_date(date):
    requests = LeaveRequest.objects.filter(date_requested=date)
    return requests

def filter_by_sick():
    return LeaveRequest.objects.filter(is_sick = True)

def filter_by_approval():
    return LeaveRequest.objects.filter(is_approved = True)

def filter_by_paid():
    return LeaveRequest.objects.filter(is_paid=True)

def filter_by_personal():
    return LeaveRequest.objects.filter(is_personal=True)

def search_employee(name, type):
    employee = LeaveRequest.objects.get(employee_name=name)
    return f"{employee} is taking a {type} leave on {employee.date_requested}"

def update_request(id,date,name,sick,personal,paid,app_by,notes):
    request = LeaveRequest.objects.get(id=id)
    request.date_requested =date,
    request.employee_name=name,
    request.is_sick=sick,
    request.is_personal=personal,
    request.is_paid=paid,
    request.approved_by=app_by,
    request.notes=notes
    request.save()
