from django.urls import path
from . import views



urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('recettes/', views.liste_recettes, name='liste_recettes'),
    path('recettes/ajouter/', views.ajouter_recette, name='ajouter_recette'),
    path('recettes/modifier/<int:pk>/', views.modifier_recette, name='modifier_recette'),
    path('recettes/supprimer/<int:pk>/', views.supprimer_recette, name='supprimer_recette'),
    path('recettes/communautaires/', views.recettes_communautaires, name='recettes_communautaires'),

]