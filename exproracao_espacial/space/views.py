from django.shortcuts import render

def home(request):
    return render(
        request,
        template_name='home.html'
    )

def philae(request):
    return render(
        request,
        template_name='philae.html'
    )