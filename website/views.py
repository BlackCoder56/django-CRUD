from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Student


# Create your views here.
def home(request):
    return render(request, 'home.html',
                  {'students': Student.objects.all()
                   })

