"""bmtc2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include

from employee import delete
from employee import update
from employee import student
from employee import studup
from employee import assign
from student import views
from college import views as v
from college import views2 as v2
from employee import viewc as vc
from bus import views as b
from employee import insert
from employee import views as a
from student import studview as sl
from student import homepage as hp
from employee import stafflogin2 as st2
from employee import assignedduties

urlpatterns = [
    path('insert-emp/',insert.insert,name='insert-emp'),
    path('admin/', admin.site.urls),
    path('stud-app',views.studss,name='stud-app'),
    path('delete-employee/',delete.delete,name='delete-emp'),
    path('update-employee/',update.update,name='update-emp'),
    path('student-approve/',student.students,name='student-approve'),
    path('student-update/',studup.update,name='update-dele-student'),
    path('college-login/',v.collegelogin,name='coll-log'),
    path('assign-duty/',assign.assigns, name='assign-duty'),
    path('bus-details/',b.buses,name='bus-details'),
    path('college-register/',v2.collreg,name='college-register'),
    path('college-approve/',vc.collreg,name='college-approve'),
    path('staff-login/',a.log,name='staff-login'),
    path('login/',a.logins,name='login'),
    path('logout/',a.logouts,name='logout'),
    path('student-login/',sl.stud_views,name='student-login'),
    path('',hp.homepage,name='homepage'),
    path('stafflogin2/',st2.stafflogins,name='stafflogin2'),
    path('assignedduties/',assignedduties.assignedduties,name='assignedduties'),


]
