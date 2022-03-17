from django.shortcuts import render

def dashboard(request):
    return render(request, 'email_fetcher/index.html')