from django.shortcuts import render
from student.models import studs
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def students(request):
    allobj=studs.objects.filter(statusc='Yes').all()
    if request.method=='POST' and 'appr' in request.POST:
        print('hey')
        usn1=request.POST.get('usn')
        ack=request.POST.get('ack')
        b=studs.objects.filter(usn=usn1).update(status='approved',ackno=ack)
        return render(request,'employee/student-approve.html',{'allobjs':allobj})

    return render(request,'employee/student-approve.html',{'allobjs':allobj})
