from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Member(models.Model):
    ROLE = [
        ('admin', 'System Admin'),
        ('manager', 'Manager'),
        ('drone', 'Drone Controller'),
        ('analyst', 'Data Analyst'),
        ('staff', 'Staff'),
    ]

    member_code = models.CharField(max_length=20, blank=True)
    member_fname = models.CharField(max_length=32)
    member_mname = models.CharField(max_length=32)
    member_lname = models.CharField(max_length=32)
    member_user = models.ForeignKey(User, on_delete=models.CASCADE)
    member_info = models.CharField(max_length=128, blank=True)
    member_role = models.CharField(max_length=20, choices=ROLE, default='staff')

    def __str__(self):
        return f"{self.member_user}"