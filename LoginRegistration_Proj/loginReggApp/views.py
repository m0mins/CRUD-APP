from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello Login App")

def login_page(request):
    diction={}
    return render(request,'loginReggApp/index.html',context=diction)