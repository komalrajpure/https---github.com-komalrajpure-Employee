from audioop import reverse
import code
from pyexpat.errors import messages
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect

import employeerecordmgmt
from .models import *
from django.contrib.auth import login,logout,authenticate
from django.utils import timezone


# Create your views here.

def index(request):
    return render(request,'index.html')

def registration(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        em = request.POST['email']
        pwd = request.POST['pwd']
        
        try:
            user = User.objects.create_user(first_name=fn, last_name=ln, username=em, password=pwd)
            EmployeeDetail.objects.create(user = user, empcode=ec,)
            error="no"
        

        except:
            error="yes"
    return render(request,'registration.html',locals())


def emp_login(request):
    error=" "
    if request.method=='POST':
        U=request.POST['emailid']
        P=request.POST['password']
        user=authenticate(username=U,password=P)
        if user:
            login(request,user)
            error="no"
        else:
            error="yes"
    return render(request,'emp_login.html',locals())


def emp_home(request):
    #first authenticate the user and then redirect to emp_home page
    if not request.user.is_authenticated:
        return redirect('emp_login')
    return render(request,'emp_home.html')


def emp_profile(request):
    error = ""
    user=request.user
    employee=EmployeeDetail.objects.get(user=user)
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        dept = request.POST['empdept']
        designation = request.POST['empdesig']
        contact = request.POST['contact']
        jdate = request.POST['jdate']
        gender = request.POST['gender']

        employee.user.first_name=fn
        employee.user.first_name=ln
        employee.empcode=ec
        employee.empdept=dept
        employee.designation=designation
        employee.contact=contact
        employee.gender=gender

        if jdate:
            employee.joiningdate = jdate

        try:
            employee.save()
            employee.user.save()
            error="no"
        
        except:
            error="yes"
    return render(request,'emp_profile.html',locals())

def emp_request_leave(request):
    error = ""
    if request.method == "POST":
        name= request.POST['name']
        email= request.POST['email']
        code = request.POST['code']
        sdate = request.POST['sdate']
        edate = request.POST['edate']
        reason= request.POST['reason']
        try:
            Emp_Request_Leave.objects.create(Name=name,Email=email, empcode=code,  Start_Date=sdate,  End_Date=edate,  Reason=reason)
            error="no"
        except:
            error="yes"
    return render(request,'emp_request_leave.html',locals())

       
def holiday(request):
   hdays=Holiday.objects.all()
   context={
       'hdays':hdays
   }
   print(context)
   return render(request,'holiday.html',context)

def emp_message(request):
   return render(request,'emp_message.html') 

def Logout(request):
    logout(request)
    return redirect('index')

def Admin_login(request):
    error=" "
    if request.method=='POST':
        U=request.POST['emailid']
        P=request.POST['password']
        user=authenticate(username=U,password=P)
        try:
          if request.user.is_superuser:
            login(request,user)
            error="no"
          else:
              error="yes"
        
        except:
            error="yes"
    return render(request,'admin_login.html',locals())
    

def Admin_home(request):
     if not request.user.is_authenticated:
      return redirect('admin_login')
     return render(request,'admin_home.html')

def Admin_view_employes(request):
    if not request.user.is_authenticated:
      return redirect('admin_login')
    employee=EmployeeDetail.objects.all()
    return render(request,'admin_view_employes.html', locals())

def Admin_leave_requests(request):
    if not request.user.is_authenticated:
      return redirect('admin_login')
   
    leave=Emp_Request_Leave.objects.all().order_by('-id')
    return render(request,'admin_messages.html', {"leave":leave})  

def leave_approve(request, id):
    context = {}
    leave = Emp_Request_Leave.objects.get(id=id)
    if leave.status == 0:
        leave.status = 1
        leave.save()
        
       
        context['status'] = 'approved'
    else:
        context['status'] = 'already approved'
    approved_leave = Emp_Request_Leave.objects.filter(status=1)
   
    return render(request, 'leave_approve.html', context)

def leave_reject(request,id): 
     context = {}
     leave = Emp_Request_Leave.objects.get(id=id)
     if leave.status == 0:
        leave.status = 2
        leave.save()
        
       
        context['status'] = 'rejected'
     else:
        context['status'] = 'already rejected'
        approved_leave = Emp_Request_Leave.objects.filter(status=2)
        return render(request, 'leave_reject.html', context)



def leave_status(request):
   
    leaves=Emp_Request_Leave.objects.filter( Email=request.user).order_by('-id')
   
    context={
        'leave':leaves
    }
 
    return render(request,'leave_status.html',context)

def admin_holiday(request):
    hdays=Holiday.objects.all()
    context={
       'hdays':hdays
   }
    
    return render(request,'admin_holiday.html',context)
    

