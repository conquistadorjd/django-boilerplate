from django.shortcuts import render, get_object_or_404, redirect

def index(request):
    context = "This is coming from view"
    return render(request, 'app1/index.html',{'context':context}) 