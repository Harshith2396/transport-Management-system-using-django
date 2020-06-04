from django.shortcuts import render
from django.http import HttpResponse
from .forms import stud_form
from datetime import datetime
from .models import studs
from college.models import college
from bus.models import routes
# Create your views here.
def studss(request):
    formc=college.objects.all()
    route=routes.objects.all()
    if request.method=='POST' and 'b1' in request.POST:
        temp=studs()
        temp.gender=request.POST.get('gender')
        date=request.POST.get('dob')
        temp.dob=datetime.strptime(date,'%Y-%m-%d').date()
        temp.email=request.POST.get('email')
        temp.usn=request.POST.get('usn')
        temp.father=request.POST.get('father')
        temp.mother=request.POST.get('mother')
        temp.college=request.POST.get('college')
        temp.name=request.POST.get('name')
        temp.start=request.POST.get('start')
        temp.destiantion=request.POST.get('destination')
        temp.changeover=request.POST.get('changeover')
        temp.address=request.POST.get('address')
        temp.phone=request.POST.get('phone')
        temp.save()
        return HttpResponse('<h1> YOU HAVE SUCCESSFULLY APPLLIED FOR BUS PASS <h1>')
        

    return render(request,'student/form.html',{"formc":formc,"route":route})
