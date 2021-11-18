from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'two_plus_two', views.two_plus_two, name='two_plus_two'),
    url(r'', views.hello, name='hello'),
    
]
