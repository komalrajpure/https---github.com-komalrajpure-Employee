from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class EmployeeDetail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    empcode = models.CharField(max_length=50)
    empdept = models.CharField(max_length=50,null=True)
    designation= models.CharField(max_length=50,null=True)
    contact= models.CharField(max_length=50,null=True)
    gender= models.CharField(max_length=50,null=True)
    joiningdate= models.DateField(null=True)
    def __str__(self):
        return self.user.username
    
   
@property
def is_staff(self):
    return self.staff


class Emp_Request_Leave(models.Model):
    Name=models.CharField(max_length=50,null=False)
    Email=models.EmailField()
    empcode=models.IntegerField()
    Start_Date=models.DateField(null=True)
    End_Date=models.DateField(null=True)
    Reason=models.CharField(max_length=100)
    status = models.IntegerField( default=0)
    def __str__(self):
        return self.Name
    
    def get_status(self):
        if self.status == 1:
            return "Approved"
        elif self.status == 2:
            return "Rejected"
        else:
            return "Pending"

    



class Holiday(models.Model):
    Date=models.DateField()
    Day=models.CharField(max_length=10)
    Name=models.CharField(max_length=50)
    def __str__(self):
        return self.Name
    