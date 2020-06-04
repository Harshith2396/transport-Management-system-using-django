from django.shortcuts import render
from .models import emp
from datetime import datetime
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def update(request):
    allobj=emp.objects.all()
    if request.method=='POST' and 'update-emp' in request.POST:
        a=request.POST.get('emp')

        up=emp.objects.get(emp_id=a)
        print('hey')
        return render(request,'employee/update.html',{'allobjs':allobj,'update':up})
    if request.method=='POST' and 'b34' in request.POST:
        print('hey')
        gender1=request.POST.get('gender')
        date=request.POST.get('dob')
        dob1=datetime.strptime(date,'%Y-%m-%d').date()
        email1=request.POST.get('email')
        emp_id1=request.POST.get('emp_id')
        father1=request.POST.get('father')
        mother1=request.POST.get('mother')
        name1=request.POST.get('name')
        designation1=request.POST.get('designation')
        address1=request.POST.get('address')
        phone1=request.POST.get('phone')
        print('hey')
        b=emp.objects.filter(emp_id=emp_id1).update(gender=gender1,dob=dob1,email=email1,father=father1,mother=mother1,name=name1,designation=designation1,
        address=address1,phone=phone1)



    return render(request,'employee/update.html',{'allobjs':allobj})
