from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from employee.models import emp
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

def logins(request):
    form=AuthenticationForm()
    if request.method=='POST' and 'loginstaff' in request.POST:
        print('hey')
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            print('hey')
            user=form.get_user()
            login(request,user)
            return redirect('insert-emp')
    return render(request,'accounts/login.html',{'form':form})
def logouts(request):
    form=AuthenticationForm()
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def log(request):
    employees=emp.objects.all()
    form=UserCreationForm()
    if request.method=='POST' and 'createuser' in request.POST:
        print('hey')
        form=UserCreationForm(request.POST)
        if form.is_valid():
            print('hey')
            form.save()
            return HttpResponse("<h1>user created succesfully<h1>")
    return render(request,'accounts/createuser.html',{'form':form,'employee':employees})
