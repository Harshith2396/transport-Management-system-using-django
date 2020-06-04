from django.shortcuts import render
from .models import emp
from datetime import datetime
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def insert(request):
    print('hey1')
    temp=emp()
    if request.method=='POST' and 'empb' in request.POST:
        print('hey2')
        temp.gender=request.POST.get('gender')
        date=request.POST.get('dob')
        temp.dob=datetime.strptime(date,'%Y-%m-%d').date()
        temp.email=request.POST.get('email')
        temp.emp_id=request.POST.get('employee')
        temp.father=request.POST.get('father')
        temp.mother=request.POST.get('mother')
        temp.name=request.POST.get('name')
        temp.designation=request.POST.get('designation')
        temp.address=request.POST.get('address')
        temp.phone=request.POST.get('phone')
        temp.save()
        return render(request,'employee/details.html')
    return render(request,'employee/details.html')
