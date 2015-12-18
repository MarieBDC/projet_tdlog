from django.shortcuts import render

# Create your views here.

# A arranger un peu comme dans le tuto pour les articles, par id
def projet(request):
	return render(request, 'projet/projet.html', locals())