"""
URL configuration for employeerecordmgmt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.urls import path
from employee import views
from employee.views import leave_status
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('registration', views.registration, name='registration'),
    path('emp_login', views.emp_login, name='emp_login'),
    path('emp_home', views.emp_home, name='emp_home'),
    path('emp_profile', views.emp_profile, name='emp_profile'),
    path('emp_request_leave', views.emp_request_leave, name='emp_request_leave'),
    path('holiday', views.holiday, name='holiday'),
    path('logout',views.Logout,name='logout'),
    path('admin_login',views.Admin_login,name='admin_login'),
    path('admin_holiday',views.admin_holiday,name='admin_holiday'),
    path('admin_home',views.Admin_home,name='admin_home'),
    path('admin_view_employes',views.Admin_view_employes,name='admin_view_employes'),
    path('admin_leave_requests',views.Admin_leave_requests,name='admin_leave_requests'),
    path('leave_approve/<int:id>/',views.leave_approve,name='leave_approve'),
    path('leave_reject/<int:id>/',views.leave_reject,name='leave_reject'),
    path('leave_status', views.leave_status, name='leave_status')
  
   


     
     
]

    


    
