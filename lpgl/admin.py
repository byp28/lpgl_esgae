from django.contrib import admin

from lpgl.models import Eleve,Livre

# Register your models here.

class EleveAdmin(admin.ModelAdmin):
    list_display = ("name")

class LivreAdmin(admin.ModelAdmin):
    list_display = ("titre","quantite","eleve")
    list_filter = ["titre"]
    search_fields  = ["titre"]
    
admin.site.register(Eleve)
admin.site.register(Livre,LivreAdmin)