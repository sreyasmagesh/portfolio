from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about',views.about, name='about'),
    path('download',views.download, name='download'),
    path('contact',views.contact, name='contact'),
    path('artwork',views.artwork, name='artwork'),
]