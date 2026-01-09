from django.db import models

# Create your models here.
class Categorie(models.Model):
    nom_categorie = models.CharField(max_length=255)

    def __str__(self):
        return self.nom_categorie



class Place(models.Model):
    nom_place = models.CharField(max_length=255)
    ville = models.CharField(max_length=255,)
    indication = models.CharField(max_length=255, default='')
    pseudo = models.CharField(max_length=25)
    categorie = models.ForeignKey(Categorie, related_name='places', on_delete=models.CASCADE)
    date_ajout = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nom_place