from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking
from django.db import connection

# Create your views here.
def HomePage1(request):
	return render(request, 'HomePage1.html') 

def signIn(request):
	return render(request, 'signIn.html') 

def Contactus(request):
	return render(request, 'Contactus.html') 

def BeautyExperts(request):
	return render(request, 'BeautyExperts.html') 

def BookingPage(request):
	return render(request, 'BookingPage.html') 

def Aboutas2(request):
	return render(request, 'Aboutas2.html') 

def salon2(request):
	return render(request, 'salon2.html') 



def reserve(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('HomePage1')  
    else:
        form = BookingForm()
    return render(request, 'BookingPage.html', {'form': form})
