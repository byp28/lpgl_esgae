from django.db import models

class Eleve(models.Model):
    name = models.CharField(max_length = 100, unique= True)
    
    class Meta:
        verbose_name = "Eleve"
        verbose_name_plural = "Eleves"
        
class Livre(models.Model):
    titre = models.CharField(max_length = 100, unique= True)
    quantite = models.IntegerField(default = 1)
    eleve  = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Livre"
        verbose_name_plural = "Livres"