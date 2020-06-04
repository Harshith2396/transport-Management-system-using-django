from django.shortcuts import render
from .forms import formc
from college.models import college
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def collreg(request):
    coll=college()
    table=college.objects.all()
    forms= college.objects.all()
    if request.method=='POST' and 'collapprove' in request.POST:
        colle=request.POST.get('college')
        print(colle)
        usernames=request.POST.get('username')
        passwords=request.POST.get('password')
        college.objects.filter(name=colle).update(username=usernames,password=passwords)
        return render(request,'employee/college-approve.html',{'forms':forms,'table':table})
    return render(request,'employee/college-approve.html',{'forms':forms,'table':table})

