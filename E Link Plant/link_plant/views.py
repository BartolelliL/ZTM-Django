from django.shortcuts import render
from .models import Profile, Link
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

class LinkListView(ListView):
    model = Link

class LinkCreateView(CreateView):
    model = Link
    fields = "__all__"
    success_url = reverse_lazy("link-list")
    
    def get(self, request):
        return render(request, "link_plant/link_form.html")

    def post(self, request):
        pass
