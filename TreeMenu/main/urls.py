from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('services/', views.services_view, name='services'),
    path('services/web-development/', views.web_development_view, name='web_development'),
    path('services/mobile-development/', views.mobile_development_view, name='mobile_development'),
    path('contact/', views.contact_view, name='contact'),
]
