from django.shortcuts import render
from django.http import HttpResponse
from .models import studs
def stud_login(request):
    print("hello")
    if request.method=='POST' and 'Login' in request.POST:
        print('hey')
        a=request.POST.get('usn')
        print('a')
        b=request.POST.get('password')
        print('b')
        students=studs.objects.filter(usn=a)
        for i in students:
            if i.phone==b:
                print('hey')
                c=i.name
                return render(request,'student/stud_details.html',{'student':students})
            else:
                return HttpResponse('<h1>Enter the usser name and password correctly</h1>')
    return render(request,'student/studlogin.html')
