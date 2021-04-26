from django.urls import path
from . import views

urlpatterns = [

path('desierto',views.desierto, name = 'desierto'),
path('presentacion',views.presentacion, name = 'presentacion'),
path('recuerdos',views.recuerdos, name = 'recuerdos'),
path('amor',views.amor, name = 'amor'),
path('voz',views.voz, name = 'voz'),
path('rachel',views.rachel, name = 'rachel'),
path('rachel2',views.rachel2, name = 'rachel2'),
path('rachel3',views.rachel3, name = 'rachel3'),
path('tormenta',views.tormenta, name = 'tormenta'),
path('opcion1',views.opcion1, name = 'opcion1'),
path('opcion2',views.opcion2, name = 'opcion2'),
path('opcion3',views.opcion3, name = 'opcion3'),
path('opcion4',views.opcion4, name = 'opcion4'),
path('etica',views.etica, name = 'etica'),
path('ser_humano',views.ser_humano, name = 'ser_humano'),
path('fotos',views.fotos, name = 'fotos'),
path('test',views.test, name = 'test'),
path('fin',views.fin, name = 'fin'),
path('chatbot',views.chatbot, name = 'chatbot')
]
