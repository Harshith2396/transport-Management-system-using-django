from django.shortcuts import render
from .models import assign
def assignedduties(request):
    duty=assign.objects.all()
    return render(request,'employee/assignedduties.htm',{'duty':duty})