from django.db import models

class Eleve(models.Model):
    name = models.CharField(max_length = 100, unique= True, verbose_name ="name")
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Eleve"
        verbose_name_plural = "Eleves"
        
class Livre(models.Model):
    titre = models.CharField(max_length = 100, unique= True, verbose_name = "titre")
    quantite = models.IntegerField(default = 1 , verbose_name = "quantite")
    eleve  = models.ForeignKey(Eleve, on_delete=models.CASCADE,verbose_name = "Eleve")
    
    def __str__(self):
        return self.titre
    class Meta:
        verbose_name = "Livre"
        verbose_name_plural = "Livres"