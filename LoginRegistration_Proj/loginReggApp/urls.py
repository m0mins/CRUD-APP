from django.urls import path
from loginReggApp import views


app_name="loginReggApp"

urlpatterns=[
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
]