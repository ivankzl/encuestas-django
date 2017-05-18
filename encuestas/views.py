# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Pregunta, Opcion
from django.shortcuts import render, reverse

# Create your views here.

def index(request):
    ultimas_preguntas = Pregunta.objects.order_by('fecha')[:5]
    context = {
        'ultimas_preguntas': ultimas_preguntas,
    }
    return render(request, 'encuestas/index.html', context)

def detail(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    return render(request, 'encuestas/detail.html', {'pregunta': pregunta})

def results(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    return render(request, 'encuestas/results.html', {'pregunta': pregunta})

def vote(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    try:
        opcion = pregunta.opcion_set.get(pk=request.POST['opcion'])
    except (KeyError, Opcion.DoesNotExist):
        # Volver a mostrar el formulario
        return render(request, 'encuestas/detail.html', {
            'pregunta': pregunta,
            'error_message': "No seleccionaste una opcion.",
        })
    else:
        opcion.votos += 1
        opcion.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('encuestas:results', args=(pregunta.id,)))
