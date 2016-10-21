from django.shortcuts import render, redirect
from ..login_reg_app.models import User
from .models import Trip
from django.contrib import messages
from django.core.urlresolvers import reverse
from datetime import datetime

# Create your views here.
def index(request):
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'trips': Trip.objects.all()
    }
    return render(request, 'travels_app/index.html', context)
def add_plan(request):
    return render(request, 'travels_app/add_plan.html')

def submit(request):
    if request.method == 'POST':
        print('validating plan')
        user = User.objects.get(id=request.session['user_id'])
        validation = Trip.objects.add_trip(request.POST, user)
        if validation[0]:
            messages.success(request, validation[1])
            return redirect(reverse('travels:index'))
        else:
            for error in validation[1]:
                messages.error(request, error)
    return redirect(reverse('travels:add_plan'))


def destination(request, trip_id):
    print(trip_id)
    Trip.objects.get(id=trip_id)
    context = {
        'trip': Trip.objects.get(id=trip_id)
    }
    return render(request, 'travels_app/destination.html')
