from django.urls import path
from loginReggApp import views


app_name="loginReggApp"

urlpatterns=[
    path('',views.index,name='index'),
    path('login_page/',views.login_page,name='login_page'),
]