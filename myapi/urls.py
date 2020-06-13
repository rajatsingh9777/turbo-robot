# myapi/urls.pyfrom django.urls import include, path
from rest_framework import routers
from . import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('home/', views.showform, name='home'),
    path('fr/', views.WorkingMovieResult.as_view(), name="fr"),
    #path('home22/', views.CustomersListView.as_view(), name = 'home22'),


]
