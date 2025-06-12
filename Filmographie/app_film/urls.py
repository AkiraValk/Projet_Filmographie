from django.urls import path

from . import views
urlpatterns = [
    path('ajout', views.ajout_Personnes),
    path('affiche', views.affiche_Personnes),
    path('traitement', views.traitement_Personnes),
    ]