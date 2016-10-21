from __future__ import unicode_literals
from django.db import models
from ..login_reg_app.models import User
from datetime import datetime
from django.utils.encoding import python_2_unicode_compatible

class TripManager(models.Manager):
    def add_trip(self, form_data, user):
        errors = []
        print(form_data['start_date'])
        if len(form_data['destination']) == 0 or len(form_data['plan']) == 0 or len(form_data['start_date']) == 0 or len(form_data['end_date']) == 0:
            errors.append("Please fill out all fields of the form!")
        if len(form_data['start_date']) > 0 or len(form_data['end_date']) > 0:
            start_date = datetime.strptime(form_data['start_date'], "%Y-%m-%d")
            end_date = datetime.strptime(form_data['end_date'], "%Y-%m-%d")
            print(start_date)
            if datetime.today() >= start_date:
                errors.append("Start date must be in the future")
            if start_date > end_date:
                errors.append("Trip end date cannot be before start date")
        if len(errors) is not 0:
            return (False, errors)
        else:
            print("passed validations")
            # add trip to the database
            trip = Trip.objects.create(destination=form_data['destination'], plan=form_data['plan'], trip_maker=user, start_date=start_date, end_date=end_date)
            trip.travelers.add(user)
            return (True, "Trip successfully added")
    def join_trip(self, trip_id, user):
        trip = Trip.objects.get(id=trip_id)
        user.trips.add(trip)
        return("Successfully added trip to your schedule!")


class Trip(models.Model):
    destination = models.CharField(max_length=255)
    plan = models.TextField()
    trip_maker = models.ForeignKey(User, related_name='trip')
    travelers = models.ManyToManyField(User, related_name='trips')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TripManager()
    def __str__(self):              # __unicode__ on Python 2
        return self.destination
