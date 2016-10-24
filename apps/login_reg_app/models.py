from __future__ import unicode_literals
from django.db import models
import bcrypt
from django.utils.encoding import python_2_unicode_compatible
#import re
#email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#found a name regex from online
#name_regex = re.compile(r'^[A-Z][-a-zA-Z]+$')


class UserManager(models.Manager):
    def login(self, form_data):
        print("Validating login")
        # retrieve the user from database using email
        user = User.objects.filter(username=form_data['username'])
        if user:
            print('Username found in database')
            user = user[0]
            if bcrypt.checkpw(form_data['pw'].encode(), user.pw_hash.encode()):
                print("passwords match")
                # returning user object to views
                return (True, user)
        return (False, "Invalid username or password")

    def register(self, form_data):
        # Validation portion. Pushes all errors to an array that is returned if there are errors
        errors = []
        # if not name_regex.match(form_data['name']):
        #     errors.append("Invalid name")
        # if not name_regex.match(form_data['username']):
        #     errors.append("Invalid username")
        if len(form_data['name']) < 3 or len(form_data['username']) < 3:
            errors.append("Name or username must be 3 or more characters in length")
        if len(form_data['pw']) < 8:
            errors.append("Password must be 8 or more characters in length")
        if form_data['pw'] != form_data['pw_confirmation']:
            errors.append("Password must match password confirmation")
        user = User.objects.filter(username=form_data['username'])
        if user:
            errors.append("Username has already been used")
        # checks if there were any errors
        if errors:
            return (False, errors)
        else:
            print("passed validations")
            # create the hashed password using bcrypt. Remember to encode
            pw_hash = bcrypt.hashpw(form_data['pw'].encode(), bcrypt.gensalt().encode())
            # create() method in objects returns newly entered entry in your db
            user = User.objects.create(username=form_data['username'], name=form_data['name'], pw_hash=pw_hash)
            return (True, user)

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    pw_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):              # __unicode__ on Python 2
        return self.name
