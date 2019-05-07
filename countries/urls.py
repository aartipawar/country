from django.urls import path
from . import views

urlpatterns = [
    # path('city/list',views.CityList.as_view()),
    # path('state/list',views.StateList.as_view()),
    path('locations',views.CountryView.as_view()),
    path('get/state',views.get_state),
    path('get/city',views.get_city),
   ]