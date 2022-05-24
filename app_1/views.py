from django.shortcuts import render


# Create your views here.
def ejemplo(request):
    return render(request, "app_1/index.html")