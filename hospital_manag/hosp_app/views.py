from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Appointment

from .forms  import AppForm


def home(request):
    return render(request,'index.html')

def TakeAppointment(request):
    form=AppForm
    return render(request, 'appointment.html', {'form':form})

def appointmentBooked(request):
    form= AppForm(request.POST)
    form.save()
    return redirect('/change')

def change(request):
    appointment=Appointment.objects.all
    return render(request, 'change.html',{'appointment':appointment})

def deleted(request,id):

    appointment= Appointment.objects.get(tell_no=id)

    appointment.delete()

    return redirect('/')
def edit(request,id):
    appointment=Appointment.objects.get(tell_no=id)
    return render(request,'edit.html',{'appointment':appointment})


def update(request, id):
    appointment=Appointment.objects.get(tell_no=id)
    form=AppForm(request.POST, instance=appointment)
    form.save()
    return redirect('/')