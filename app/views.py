from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def School_Creation(request):
    SO=SchoolForm()
    d={'SO':SO}
    if request.method=='POST':
        SD=SchoolForm(request.POST)
        if SD.is_valid():
            sn=SD.cleaned_data['sname']
            sp=SD.cleaned_data['sprinciple']
            sl=SD.cleaned_data['slocation']
            se=SD.cleaned_data['email']
            sre=SD.cleaned_data['reenteremail']
            SDO=School.objects.get_or_create(sname=sn,sprinciple=sp,slocation=sl,email=se,reenteremail=sre)[0]
            SDO.save()
            return HttpResponse('data is inserted into School table')
        else:
            return HttpResponse('invalid data')

            
    return render(request,'School_Creation.html',d)