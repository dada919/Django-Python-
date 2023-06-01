from django.shortcuts import render

from django.shortcuts import render
from .models import Membre

def inscription(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        mot_de_passe = request.POST.get('mot_de_passe')
        
        membre = Membre(nom=nom, mot_de_passe=mot_de_passe)
        membre.save()
        
        return render(request, 'connexion.html')
    
    return render(request, 'inscription.html')

