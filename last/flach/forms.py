from django import forms
from .models import Auteur, Livre

class someforms(forms.ModelForm):
    auteur=forms.ModelChoiceField(queryset=Auteur.objects.all(),)
    
    class Meta:
        model=Livre
        fields=['titre', 'auteur','quantite']
        search_fields=("titre",)
        