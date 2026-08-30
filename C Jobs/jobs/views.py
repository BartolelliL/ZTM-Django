from django.shortcuts import render
from .models import JobsPosting

# Create your views here.
def index(request):
    active_jobs = JobsPosting.objects.filter(is_active=True)

    context: dict = {
        "job_postings": active_jobs
    }

    return render(request, "jobs/index.html", context)