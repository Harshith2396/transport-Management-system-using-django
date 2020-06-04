from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models  import emp
from .models import assign
def stafflogins(request):
    if request.method=='POST' and 'staffloginduty' in request.POST:
        a=request.POST.get("staffloginid")
        b=request.POST.get("staffloginpassword")
        print(b)
        user=emp.objects.filter(emp_id=a)
        for i in user:
            print(i.emp_id)
            if i.phone==b:
                print(1)
                if i.designation=='Driver':
                    print(1)
                    datei=request.POST.get('date-st')
                    dates=datetime.strptime(datei,'%Y-%m-%d').date()
                    assigns=assign.objects.raw('select * from employee_assign where date=%s and driver=%s',[dates,a])
                    print('hwy')
                    for j in assigns:
                        print('hey')
                        print(j.date)
                        print(j.conductor)
                        print('end')
                    return render(request,'employee/dutiescheck.htm',{'user':i,'assign':assigns})
                elif i.designation=='Conductor':
                    print(1)
                    date=request.POST.get('date-st')
                    dates=datetime.strptime(date,'%Y-%m-%d').date()
                    assigns=assign.objects.raw('select * from employee_assign where date=%s and conductor=%s',[dates,a])
                    print('hwy')
                    for j in assigns:
                        print('hey')
                        print(j.date)
                        print(j.conductor)
                        print('end')
                    return render(request,'employee/dutiescheck.htm',{'user':i,'assign':assigns})
            else:
                return HttpResponse("<h1>Incorrect Login<h1>")
    return render(request,'employee/stafflogin.htm')