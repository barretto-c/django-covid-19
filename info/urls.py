from django.urls import path
from info import views
from info.views import viewsets
from info.models import CovidData

#REST
from django.conf.urls import url, include
from django.contrib.auth.models import User, Group
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'covid/data', views.CovidDataViewSet)

urlpatterns = [
    # path("", home_list_view, name="home"),
    path("",views.HomeListViewNew.as_view() , name="home-new"),
    path("info/covid_createv2",views.CovidDataCreateViewV2.as_view() , name="covid-newv2"),
    
    path("info/about/", views.about, name="about"),
    path("info/contact/", views.contact, name="contact"),

    path("logdata/", views.logdata, name="logdata"),
    
    url(r'^', include(router.urls)),
    #url(r"^api/", include((router.urls, "rest_api"))),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))    

]