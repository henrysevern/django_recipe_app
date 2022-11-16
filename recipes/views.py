from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse ("<h1>Welcome to my recipes app!</h1>")


def about(request):
    return HttpResponse ("<h1>This about my recipe app!</h1>")
