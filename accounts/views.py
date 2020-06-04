from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from employee.models import emp
def log(request):
    employees=emp.objects.all()
    form=UserCreationForm()
    if request.method=='POST' and 'createuser' in request.POST:
        print('hey')
        form=UserCreationForm(request.POST)
        if form.is_valid():
            print('hey')
            form.save()
    return render(request,'accounts/createuser.html',{'form':form,'employee':employees})
def login(request):
    form=AuthenticationForm()
    if request.method=='POST' and 'loginstaff' in request.POST:
        print('hey')
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            print('hey')
            return render(request,'employee/insert.html')
    return render(request,'accounts/login.html',{'form':form})
