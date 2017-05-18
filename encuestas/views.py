# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Pregunta, Opcion
from django.template import loader

# Create your views here.

def index(request):
    # return HttpResponse("Hola, pagina principal.")
    latest_question_list = Pregunta.objects.order_by('-fecha')[:5]
    template = loader.get_template('encuestas/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, pregunta_id):
    return HttpResponse("Estás votando en la pregunta %s." % pregunta_id)

def results(request, pregunta_id):
    response = "Estás mirando los resultados de la pregunta %s."
    return HttpResponse(response % pregunta_id)

def vote(request, pregunta_id):
    return HttpResponse("Estás votando en la pregunta %s." % question_id)
