from django.shortcuts import render
from .models import bus
from .models import  routes
def buses(request):
    print('hey')
    buss=bus()
    r=routes()
    if request.method=='POST' and 'bus_button' in request.POST:

        buss.bus_no=request.POST.get('bus_no')

        buss.bus_stand_name=request.POST.get('bus_stand_name')
        buss.bus_service_years=request.POST.get('bus_service_years')
        buss.save()
    if request.method=='POST' and 'routes_button' in request.POST:
        r.start=request.POST.get('start')
        r.destination=request.POST.get('destination')
        r.changeover=request.POST.get('change')
        r.save()
    return render(request,'bus/bus.html')
