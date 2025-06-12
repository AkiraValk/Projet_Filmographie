# Create your models here.
from django.db import models

class Personnes(models.Model):
    type = models.CharField(blank=True, max_length=100)
    #identifiant_pers = models.ForeignKey("commentaire", on_delete=models.CASCADE, default=None)
    pseudo = models.CharField(blank=True, max_length=100)
    nom_prenom = models.CharField(blank=True, max_length=100)
    mail = models.CharField(blank=True, max_length=100)
    mot_de_passe = models.CharField(blank=True, max_length=10)

    def __str__(self):
        chaine = f"Cette personne est : {self.nom_prenom}, son mail est : {self.mail}, et son pseudo est : {self.pseudo}"
        return chaine

    def dico(self):
        return {"Type": self.type, "Pseudo": self.pseudo, "Nom et Prenom": self.nom_prenom, "mail": self.mail, "Mot de passe": self.mot_de_passe}