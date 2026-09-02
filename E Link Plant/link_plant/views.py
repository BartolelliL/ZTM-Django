from django.shortcuts import render
from .models import Profile, Link
from django.views.generic import ListView

class LinkListView(ListView):
    model = Link