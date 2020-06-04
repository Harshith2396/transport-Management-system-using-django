from django.shortcuts import render
from student.models import studs
from datetime import datetime
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def update(request):
    allobjs=studs.objects.all()
    if request.method=='POST' and 'retrieve' in request.POST:
        a=request.POST.get('up')
        allobj=studs.objects.get(usn=a)
        print('hey')
        return render(request,'employee/update-delete.html',{'allobjs':allobjs,'allobj':allobj})
    if request.method=='POST' and 'dele' in request.POST:
        print('hey')
        a=request.POST.get('up')
        studs.objects.get(usn=a).delete()
        return render(request,'employee/update-delete.html',{'allobjs':allobjs})
    if request.method=='POST' and 'update-students' in request.POST:
        print('hey')
        usn1=request.POST.get('usn')
        print(usn1)
        email1=request.POST.get('email')
        print(email1)
        father1=request.POST.get('father')
        print(father1)
        mother1=request.POST.get('mother')
        name1=request.POST.get('name')
        phone1=request.POST.get('phone')
        print('hey')
        studs.objects.filter(usn=usn1).update(email=email1,father=father1,mother=mother1,name=name1,phone=phone1)



    return render(request,'employee/update-delete.html',{'allobjs':allobjs})
