from django.shortcuts import render

def index(request):

    context: dict = {
        "movies": [
            "gladiator",
            "GLADIATOR",
            "Gladiator"
        ],
    }

    return render(request, "movies/index.html", context=context)

def about(request):
    return render(request, "movies/about.html", {})