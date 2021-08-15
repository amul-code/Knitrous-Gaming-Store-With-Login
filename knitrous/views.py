from django.shortcuts import render ,HttpResponse
from datetime import date, datetime
from knitrous.models import Contact
from knitrous.models import Clan
from django.contrib import messages

# Create your views here.
def index(request):
    # return HttpResponse("This MY Homepage")
    
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This Is About PAge")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is services page")

def contact(request):
    if request.method == 'POST':
        first = request.POST.get('first')
        last = request.POST.get('last')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(first=first, last=last, phone=phone, email=email, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your Request Submitted Successfully.')

    return render(request, 'contact.html')
    # return HttpResponse("this is Contact
    #  Page")
def games(request):
    return render(request, 'games.html')
    # return HttpResponse("this is Contact
    #  Page")
def accessories(request):
    return render(request, 'accessories.html')
def es(request):
    return render(request, 'es.html')
def clan(request):
    if request.method == 'POST':
        first = request.POST.get('first')
        last = request.POST.get('last')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        clan = Clan(first=first, last=last, phone=phone, email=email, desc=desc, date=datetime.today())
        clan.save()
        messages.success(request, 'Your Request Submitted Successfully.')
    return render(request, 'clan.html')
def login(request):
    return render(request,'login.html')