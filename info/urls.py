from django.urls import path
from info import views
from info.models import CovidData

#REST
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from django.contrib import admin


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

home_list_view = views.HomeListView.as_view(
    queryset=CovidData.objects.order_by(), 
    context_object_name="message_list",
    template_name="info/home.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path('admin/', admin.site.urls),

    path("info/<region>", views.dashboard, name="dashboard"),
    
    path("info/about/", views.about, name="about"),
    path("info/contact/", views.contact, name="contact"),

    path("logdata/", views.logdata, name="logdata"),
    
    #url(r'^', include(router.urls)),
    url(r"^api/", include((router.urls, "rest_api"))),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))    

]