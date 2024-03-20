from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    context={
        "message": "Bonjour esgae",
        "lpliste": ["orange","anans","pomme"]
        }
    template = loader.get_template("lpgl/index.html")
    return HttpResponse(template.render(context, request))

