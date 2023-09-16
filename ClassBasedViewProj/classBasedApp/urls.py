from django.urls import path
from classBasedApp import views

app_name="classBasedApp"

urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
    path('musician_details/<pk>/',views.MusicianDetail.as_view(),name='musician_details'),
    path('add_musician/',views.AddMusician.as_view(),name='add_musician'),
    path('update_musician/<pk>/',views.UpdateMusician.as_view(),name='update_musician'),
    path('delete_musician/<pk>/',views.DeleteMusician.as_view(),name='delete_musician'),

]