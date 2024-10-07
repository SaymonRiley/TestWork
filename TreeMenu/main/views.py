from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def services_view(request):
    return render(request, 'services.html')

def contact_view(request):
    return render(request, 'contact.html')

def web_development_view(request):
    return render(request, 'web_development.html')

def mobile_development_view(request):
    return render(request, 'mobile_development.html')
