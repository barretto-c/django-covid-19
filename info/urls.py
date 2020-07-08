from django.urls import path
from info import views
from info.models import CovidData

home_list_view = views.HomeListView.as_view(
    queryset=CovidData.objects.order_by(), 
    context_object_name="message_list",
    template_name="info/home.html",
)

urlpatterns = [
    #path("", views.home, name="home"),
    path("", home_list_view, name="home"),
    
    path("info/<region>", views.dashboard, name="dashboard"),
    
    path("info/about/", views.about, name="about"),
    path("info/contact/", views.contact, name="contact"),

    path("logdata/", views.logdata, name="logdata"),


]