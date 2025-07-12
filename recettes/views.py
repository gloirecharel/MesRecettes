from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import InscriptionForm, ConnexionForm, RecetteForm
from .models import Recette
from django.shortcuts import get_object_or_404

def accueil(request):
    return render(request, 'recettes/accueil.html')

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('liste_recettes')
    else:
        form = InscriptionForm()
    return render(request, 'recettes/inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        form = ConnexionForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('liste_recettes')
    else:
        form = ConnexionForm()
    return render(request, 'recettes/connexion.html', {'form': form})

@login_required
def deconnexion(request):
    logout(request)
    return redirect('accueil')

@login_required
def liste_recettes(request):
    recettes = Recette.objects.filter(cuisinier=request.user)
    return render(request, 'recettes/liste_recettes.html', {'recettes': recettes})

@login_required
def ajouter_recette(request):
    if request.method == 'POST':
        form = RecetteForm(request.POST, request.FILES)
        if form.is_valid():
            recette = form.save(commit=False)
            recette.cuisinier = request.user
            recette.save()
            return redirect('liste_recettes')
    else:
        form = RecetteForm()
    return render(request, 'recettes/ajouter_recette.html', {'form': form})


@login_required
def modifier_recette(request, pk):
    recette = get_object_or_404(Recette, pk=pk, cuisinier=request.user)
    if request.method == 'POST':
        form = RecetteForm(request.POST, request.FILES, instance=recette)
        if form.is_valid():
            form.save()
            return redirect('liste_recettes')
    else:
        form = RecetteForm(instance=recette)
    return render(request, 'recettes/modifier_recette.html', {'form': form})

@login_required
def supprimer_recette(request, pk):
    recette = get_object_or_404(Recette, pk=pk, cuisinier=request.user)
    if request.method == 'POST':
        recette.delete()
        return redirect('liste_recettes')
    return render(request, 'recettes/supprimer_recette.html', {'recette': recette})

@login_required
def recettes_communautaires(request):
    recettes = Recette.objects.exclude(cuisinier=request.user)
    return render(request, 'recettes/recettes_communautaires.html', {'recettes': recettes})

