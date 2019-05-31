from django.shortcuts import render
from .models import Destination,Discount, Testimonials
# Create your views here.


def index(request):
    
    dests = Destination.objects.all()
    
    discs = Discount.objects.all()

    tests = Testimonials.objects.all()




    return render(request, "index.html", {'dests': dests,'discs':discs,'tests':tests})

    # return render(request, "index.html", {'discs': discs})

