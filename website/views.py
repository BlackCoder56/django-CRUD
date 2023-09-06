from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Student


# Create your views here.
def home(request):
    return render(request, 'home.html',
                  {'students': Student.objects.all()
                   })


def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('home'))
