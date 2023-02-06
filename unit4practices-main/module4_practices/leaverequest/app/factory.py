import factory
from django.contrib.auth.models import User

from app.models import LeaveRequest

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = LeaveRequest

    date_requested = "x"
    employee_name = "x"
    is_sick = True
    is_paid = True
    is_approved = True
    approved_by = "x"
    notes = "x"