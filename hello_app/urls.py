from django.urls import path

from . import views

urlpatterns = [
    path(r'two_plus_two', views.two_plus_two, name='two_plus_two'),
    path(r'', views.hello, name='hello'),
    
]
