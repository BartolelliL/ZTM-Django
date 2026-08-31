from django.shortcuts import render, get_object_or_404
from .models import JobsPosting

# Create your views here.

# Il modello carica nel db le classi create.
# Tramite le views si prendono gli oggetti del modello
# e si filtrano. Questi ultimi vengono assegnati ad
# una chiave nel context:dict, che viene passata come parametro
# al modulo render

def index(request):
    active_jobs = JobsPosting.objects.filter(is_active=True)

    context: dict = {
        # This key can be accesed by the HTML
        "job_postings": active_jobs
    }

    return render(request, "jobs/index.html", context)

def job_detail(request, pk):
    job_posting = get_object_or_404(JobsPosting, pk=pk, is_active=True)

    context: dict = {
        "posting": job_posting,
    }

    return render(request, "jobs/detail.html", context)