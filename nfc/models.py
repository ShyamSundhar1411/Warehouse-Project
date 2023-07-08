from .choices import *
from django.db import models

# Create your models here.
class NFCUser(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    nfc_serial = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=100)
    club = models.CharField(max_length=100)
    faculty_registered = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.username

class Meeting(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    club = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
class Attendance(models.Model):
    meeting = models.ForeignKey(Meeting,on_delete=models.CASCADE)
    user = models.ForeignKey(NFCUser,on_delete=models.CASCADE)
    status = models.CharField(max_length=100,choices = ATTENDANCE_STATUS)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.user.username)+"-"+str(self.date)