from django.urls import path
from . import views

app_name='vote'



urlpatterns=[
    path('index/',views.index,name='index'),
]