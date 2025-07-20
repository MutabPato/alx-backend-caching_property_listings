from django.urls import path, include
from .views import property_list


urlpatterns = [
    path('property-list/', property_list, name='properties')
]