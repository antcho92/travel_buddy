from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    return redirect(reverse('users:index'))
