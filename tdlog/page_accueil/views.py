from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def accueil(request):
	return render(request, 'page_accueil/accueil.html', locals())
