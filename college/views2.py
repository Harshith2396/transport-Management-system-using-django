from django.shortcuts import render
from .forms import formc
from.models import college
def collreg(request):
    forms=formc()
    if request.method=='POST' and 'collreg' in request.POST:
        forms1=formc(request.POST)
        if forms1.is_valid():
            forms1.save()
            return render(request,'college/college-register.html',{'forms':forms})
    return render(request,'college/college-register.html',{'forms':forms})
