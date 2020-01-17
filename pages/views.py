
from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Participant

# Create your views here.
def index(request):
    return render(request,'pages/index.html')

def happysnapper(request):
    return render(request,'pages/happysnapper.html')

def tagnwin(request):
    return render(request,'pages/tagnwin.html')

def papertechrix(request):
    return render(request,'pages/papertechrix.html')

def mindopedias(request):
    return render(request,'pages/mindopedias.html')

def blackbox(request):
    return render(request,'pages/blackbox.html')

def retrofitzz(request):
    return render(request,'pages/retrofitzz.html')

def projectcorner(request):
    return render(request,'pages/projectcorner.html')

def warriorsunite(request):
    return render(request,'pages/warriorsunite.html')

def offers(request):
    return render(request,'pages/offers.html')

def miraclebombshell(request):
    return render(request,'pages/miraclebombshell.html')

def funtasktik(request):
    return render(request,'pages/funtasktik.html')

def triathlon(request):
    return render(request,'pages/triathlon.html')

def workshop(request):
    return render(request,'pages/workshop.html')

def register(request):
    if request.method == "POST":
        name = request.POST["name"]
        college = request.POST["college"]
        email = request.POST["email"]
        dept = request.POST["dept"]
        phone = request.POST["phone"]
        year = request.POST["year"]
        if request.POST["Food"] == 'Non-Veg':
            food = True 
        else:
            food = False
        if not Participant.objects.filter(email=email).exists():
            participant = Participant(name=name,email=email,college=college,department=dept,mobile=phone,year=year,non_veg=food)
            participant.save()
            regid = Participant.objects.filter(email=email)[0].id
            body = 'Dear '+name+',\n Thank you for registering in MEACONT20. Your registration number is #'+str(regid)
            send_mail('Thank you for registering',
            body,'meacont20@gmail.com',[email],fail_silently=True)
            body = 'Reg no.: '+str(regid)+'Name: '+name+'\n Email: '+email+'\n Dept: '+dept+'\n College: '+college+'\n Year: '+year+'\n Mobile no.: '+phone
            send_mail('Thank you for registering',
            body,'meacont20@gmail.com',['meaconregt20@gmail.com'],fail_silently=True)
            messages.success(request,'Registration Successful, Please check your email')
            return redirect('index')
        else:
            messages.error(request,'This email has already been registered')
            return redirect('register')
    return render(request,'pages/register.html')