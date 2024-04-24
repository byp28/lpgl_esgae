from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from lpgl.models import Livre


def index(request):
    context={
        "livres" : Livre.objects.all()
      #  "message": "Bonjour esgae",
      #  "lpliste": ["orange","anans","pomme"]
        }
    #template = loader.get_template("lpgl/index.html")
    #return HttpResponse(template.render(context, request))
    return render(request, "lpgl/index.html", context)

