from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from classBasedApp import models
from django.urls import reverse_lazy

# Create your views here.
class IndexView(ListView):
    context_object_name='musician_list'
    model=models.Musician
    template_name='classBasedApp/index.html'

class MusicianDetail(DetailView):
    context_object_name='musicians'
    model=models.Musician
    template_name='classBasedApp/musician_details.html'

class AddMusician(CreateView):
    fields=('first_name','last_name','instrument')
    model=models.Musician
    template_name='classBasedApp/musician_form.html'


class UpdateMusician(UpdateView):
    fields=('first_name','last_name','instrument')
    model=models.Musician
    template_name='classBasedApp/musician_form.html'

class DeleteMusician(DeleteView):
    context_object_name='musician'
    model=models.Musician
    success_url=reverse_lazy('classBasedApp:index')
    template_name='classBasedApp/delete_musician.html'



    
        