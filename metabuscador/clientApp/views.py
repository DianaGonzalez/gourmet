#encoding: utf-8
from django.db.models.query_utils import Q
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template.context import RequestContext
from clientApp.models import Record

class MyException:
    def __str__(self):
        return "Lanzada nuestra excepcion"

def home(request):

    return render_to_response('index.html', request.session, context_instance=RequestContext(request))

def search(request):

    keywords = request.GET.get('keywords',' ')
    if keywords == '':
        raise NameError, "No se introdujo una palabra para realizar la  búsqueda"
    else:
        records = Record.objects.filter(
            Q(url__icontains=keywords)|
            Q(descripcion__icontains=keywords)|
            Q(titulo__icontains=keywords)|
            Q(pclav__icontains=keywords)
        )
        template="results.html"
    return render_to_response(template, {'keywords':keywords, 'results':records}, context_instance=RequestContext(request))