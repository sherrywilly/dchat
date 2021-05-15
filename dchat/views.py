from django.http.response import HttpResponse
from django.shortcuts import render


def Tester(request):
    context = {

    }
    return render(request, "index.html", context)
