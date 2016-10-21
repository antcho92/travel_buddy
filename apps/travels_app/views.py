from django.shortcuts import render, redirect
from ..login_reg_app.models import User
from .models import Trip
from django.contrib import messages
from django.core.urlresolvers import reverse
from datetime import datetime

# Create your views here.
def index(request):
    if 'user_id' in request.session:
        user = User.objects.get(id=request.session['user_id'])
        context = {
            'user': user,
            'trips': Trip.objects.all().exclude(travelers=user)
        }
        return render(request, 'travels_app/index.html', context)
    else:
        return redirect(reverse('users:index'))

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
    trip = Trip.objects.get(id=trip_id)
    users = trip.travelers.all().exclude(id=request.session['user_id'])
    for user in users:
        print(user.name)
    print(trip)
    context = {
        'trip': Trip.objects.get(id=trip_id),
        'users': users
    }
    return render(request, 'travels_app/destination.html', context)

def join(request, trip_id):
    print("trying to join")
    user = User.objects.get(id=request.session['user_id'])
    validation = Trip.objects.join_trip(trip_id, user)
    messages.success(request, validation)
    return redirect(reverse('travels:index'))
