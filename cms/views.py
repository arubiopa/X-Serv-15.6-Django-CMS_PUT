from django.shortcuts import render
from models import Pages
from django.http import HttpResponse,HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def cms(request, recurso):
    if request.method == "GET":
        try:
    		contenido = Pages.objects.get(name=recurso)
    		return HttpResponse(contenido.name+ ':' + contenido.page)
    	except Pages.DoesNotExist:
    		return HttpResponseNotFound("Recurso no encontrado: " + recurso)

    if request.method == "PUT":
        pagina = Pages(name=recurso, page=request.body)
        pagina.save()
        return HttpResponse("Pagina guardada: "+ request.body)
