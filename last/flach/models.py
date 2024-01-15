from django.db import models

class Auteur(models.Model):
    nom=models.CharField(max_length=233)
    def __str__(self) :
        return self.nom


class Livre(models.Model):
    titre=models.CharField(max_length=33)
    auteur=models.ForeignKey(Auteur, on_delete=models.CASCADE)
    quantite=models.IntegerField(default=0)
    
    def __str__(self) :
        return self.titre

