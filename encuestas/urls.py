from django.conf.urls import url
from . import views

urlpatterns = [
    # ejemplo: /encuestas/
    url(r'^$', views.index, name='index'),
    # ejemplo: /encuestas/5/
    url(r'^(?P<pregunta_id>[0-9]+)/$', views.detail, name='detail'),
    # ej: /encuestas/5/results/
    url(r'^(?P<pregunta_id>[0-9]+)/results/$', views.results, name='results'),
    # ejemplo: /encuestas/5/vote/
    url(r'^(?P<pregunta_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
