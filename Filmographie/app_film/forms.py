from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class PersonnesForm(ModelForm):
    class Meta:
        model = models.Personnes
        fields = ('type', 'pseudo', 'nom_prenom', 'mail', 'mot_de_passe')
        labels = {
            'type': _('Type'),
            'pseudo': _('Pseudo'),
            'nom_prenom': _('Nom et Prénom'),
            'mail': _('Adresse mail'),
            'mot_de_passe': _('Mot de passe')
        }