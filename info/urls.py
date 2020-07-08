from django.urls import path
from info import views

urlpatterns = [
    path("", views.home, name="home"),
    path("info/<region>", views.dashboard, name="dashboard"),
    
    path("info/about/", views.about, name="about"),
    path("info/contact/", views.contact, name="contact"),
]