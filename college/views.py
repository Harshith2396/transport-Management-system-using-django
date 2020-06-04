from django.shortcuts import render,redirect
from django.http import HttpResponse
from  .models import college
from student.models import studs
def collegelogin(request):
    if request.method=='POST' and 'login' in request.POST:
        user=request.POST.get('user')
        password=request.POST.get('password')
        print('hey')
        paas1=college.objects.filter(username=user).all()
        for i in paas1:
            b=i.name
            if i.password == password:
                return render(request,'college/college.html',{'collegename':b})
            else:
                return HttpResponse('<h> incorrect <h>')
    if request.method=='POST' and 'appr' in request.POST:
        usns=request.POST.get('usn')
        college1=request.POST.get('coll')
        studs.objects.filter(usn=usns).update(statusc='Yes')
        allobjs=studs.objects.filter(college=college1,statusc='No')

        return render(request,'college/college.html',{'allobjs':allobjs,'collegename':college1})
    if request.method=='POST' and 'show' in request.POST:
        college1=request.POST.get('coll')
        allobjs=studs.objects.filter(college=college1,statusc='No').all()
        print(college1)
        return render(request,'college/college.html',{'allobjs':allobjs,'collegename':college1})
    return render(request,'college/college-login.html')
