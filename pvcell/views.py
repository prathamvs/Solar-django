from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Points,Data,Image
from django.contrib.auth.models import User,auth

# Create your views here.
def home(request):
    imgs  = Image.objects.all()    
    return render(request,'index.html',{'imgs':imgs});

def camera(request):
    imgs  = Image.objects.all()  
    return render(request,'live-cameras.html',{'imgs':imgs});

def about(request):
    return render(request,'about.html');

def contact(request):
    return render(request,'contact.html');

def analysis(request):
    return render(request,'analysis.html');

def overview(request):
    points = Points.objects.all()
    return render(request,'dashboard.html',{'points':points});


def report(request):
    
    data1 = Data()
    data1.area = 'Area 1'
    data1.DCvolt = 136.7
    data1.ACvolt = 0
    data1.DCcurrent = 15.3
    data1.ACcurrent = 0
    data1.DCPower = 2.1
    data1.ACpower = 1.9
    data1.energy = 4.6
    data1.current = 'error'
    data1.irradiance = 'error'
    
    data2 = Data()
    data2.area = 'Area 2'
    data2.DCvolt = 136.7
    data2.ACvolt = 10
    data2.DCcurrent = 15.3
    data2.ACcurrent = 0
    data2.DCPower = 2.7
    data2.ACpower = 1.3
    data2.energy = 5.6
    data2.current = 'Perfect'
    data2.irradiance = 'Good'
    
    data3 = Data()
    data3.area = 'Area 3'
    data3.DCvolt = 132.7
    data3.ACvolt = 0
    data3.DCcurrent = 14.3
    data3.ACcurrent = 0
    data3.DCPower = 2.1
    data3.ACpower = 1.9
    data3.energy = 5.6
    data3.current = 'error'
    data3.irradiance = 'Perfect'
    
    data4 = Data()
    data4.area = 'Area4'
    data4.DCvolt = 35.7
    data4.ACvolt = 0
    data4.DCcurrent = 15.3
    data4.ACcurrent = 0
    data4.DCPower = 2.1
    data4.ACpower = 5.0
    data4.energy = 4.6
    data4.current = 'Good'
    data4.irradiance = 'Perfect'
    
    datas = [data1,data2,data3,data4]
    
    return render(request,'report.html',{'datas':datas});





