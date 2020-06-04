from django.shortcuts import render
from .models import emp
import sqlite3
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def delete(request):
    allobj=emp.objects.all()

    if request.method=='POST' and 'dele-emp' in request.POST:
        emp1=request.POST.get('emp')
        print('hry')
        emp.objects.filter(emp_id=emp1).delete()

    return render(request,'employee/delete.html',{'allobjs':allobj})
