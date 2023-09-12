from django.shortcuts import render
from django.http import HttpResponse
from CrudApp.models import Musician,Album
from CrudApp import forms
from django.db.models import Avg

# Create your views here.
def index(request):
    musician_list=Musician.objects.order_by('first_name')
    diction={'title':"Home Page",'musicians':musician_list}
    return  render(request ,'CrudApp/index.html', context=diction)


def album_form(request):
    form=forms.AlbumForm()
    if request.method=='POST':
        form=forms.AlbumForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    diction={'title':"Add Album",'album_form':form}
    return render(request,'CrudApp/album_form.html',context=diction)


def musician_form(request):
    form=forms.MusicianForm()
    if request.method=='POST':
        form=forms.MusicianForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction={'title':"Add Musician ",'musician_form':form}
    return render(request,'CrudApp/musician_form.html',context=diction)


def album_list(request,artist_id):
    artist_info=Musician.objects.get(pk=artist_id)
    album_list=Album.objects.filter(artist=artist_id).order_by('name','release_date')
    artist_rating=Album.objects.filter(artist=artist_id).aggregate(Avg('num_stars'))
    diction={'title':"List of Albums",'artist_info':artist_info,'album_list':album_list,'artist_rating':artist_rating}
    return render(request,'CrudApp/album_list.html',context=diction)
   

def edit_artist(request,artist_id):
    artist_info=Musician.objects.get(pk=artist_id)
    form=forms.MusicianForm(instance=artist_info)
    if request.method=='POST':
        form=forms.MusicianForm(request.POST,instance=artist_info)
        if form.is_valid():
            form.save(commit=True)
            return album_list(request,artist_id)

    diction={'edit_form':form}
    return render(request,'CrudApp/edit_artist.html',context=diction)

def edit_album(request,album_id):
    album_info=Album.objects.get(pk=album_id)
    form=forms.AlbumForm(instance=album_info)

    diction={}
    if request.method=='POST':
        form=forms.AlbumForm(request.POST,instance=album_info)
        if form.is_valid():
            form.save(commit=True)
            diction.update({'success_text':"Successfully Updated !!"})


    diction.update({'edit_form':form})
    return render(request ,'CrudApp/edit_album.html', context=diction)