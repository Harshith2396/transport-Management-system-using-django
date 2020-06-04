from django.shortcuts import render
from bus.models import bus,routes
from .models import assign,emp
from datetime import datetime
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def assigns(request):
    print('hey')
    assigne=assign()
    route=routes.objects.all()
    buses=bus.objects.all()
    drivers=emp.objects.filter(designation='Driver')
    conductors=emp.objects.filter(designation='Conductor')
    if request.method=='POST' and 'assign-staff' in request.POST:
        print('hey')
        dates=request.POST.get('date')
        print(dates)
        dat=datetime.strptime(dates,'%Y-%m-%d').date()
        assigne.date=dat
        assigne.start=request.POST.get('start')
        assigne.destination=request.POST.get('destination')
        d=request.POST.get('drivers')
        assigne.driver=d
        c=request.POST.get('conductors')
        assigne.conductor=c
        assigne.bus_no=request.POST.get('busnums')
        e=emp.objects.filter(emp_id=d)
        f=emp.objects.filter(emp_id=c)
        for i in f:
            assigne.conductor_name=i.name
        for i in e :
            assigne.driver_name=i.name
        assigne.save()
    return render(request,'employee/staff-duties-assign.html',{'routes':route,'buses':buses,'drivers':drivers,'conductors':conductors})
