from django.contrib import admin

from lpgl.models import Eleve,Livre,Bibliotheque

# Register your models here.

class EleveAdmin(admin.ModelAdmin):
    list_display = ("name")

class BibliothequeAdmin(admin.ModelAdmin):
    list_display = ("Libele")
    
class LivreAdmin(admin.ModelAdmin):
    list_display = ("titre","quantite","eleve")
    list_filter = ["titre"]
    search_fields  = ["titre"]
    
admin.site.register(Eleve)
admin.site.register(Bibliotheque)
admin.site.register(Livre,LivreAdmin)