from django.urls import path
from . import views

app_name='menu'



urlpatterns=[
    path('index/',views.index,name='index'),
    path('dish/',views.dish,name='dish'),
    path('pasta/',views.pasta,name='pasta'),
    path('risotto/',views.risotto,name='risotto'),
    path('drink/',views.drink,name='drink'),
    path('detail/<mpk>',views.detail,name='detail'),
    path('create/',views.create,name='create'),
    path('delete/<mpk>',views.delete,name='delete'),
]