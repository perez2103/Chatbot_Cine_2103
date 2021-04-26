from django.db import models

# Create your models here.
from os import system
import win32com.client 
speaker = win32com.client.Dispatch ("SAPI.SpVoice")
'''
class Custom(object):

    def setattr_custom(self, atrib, valor):
        setattr(self, atrib, valor)
'''
class CienciaFiccion(models.Model):
    nombre = models.CharField(max_length=100)
    dic_peliculas_cf = models.CharField(max_length=100)
    titulos = models.CharField(max_length=100)

    def entrada():
        print('¿Te gusta la ciencia ficción?')
        pregunta = input('¿Te gustó regreso al futuro?:')
        cadena = (pregunta)
        return cadena


    def __str__(self):
        return f'SUBGENERO :{self.id}-{self.nombre} {self.titulos} '



class PeliculasCiencia(models.Model):

    nombre = models.CharField(max_length=100)
    puntuacion = models.CharField(max_length=100)
    titulos = models.CharField(max_length=100)
    fk_ciencia_ficcion = models.ForeignKey(CienciaFiccion,on_delete = models.CASCADE,blank = True)

    def hola(self):
        print('hola')
    

    def __str__ (self):
        cadena = f'TITULO:{self.id}-{self.nombre}-PUNTUACION:  {self.puntuacion} '

        return cadena

      


'''

def pausa():
    input('presione enter para continuar...') 




def agregar_subgenero(dic_peliculas_cf):

    nombre = input('Dime un subgenero dentro de la ciencia ficción que te haya gustado:')
    puntuacion = input('Puntua del 0 al 10 ese subgenero:')


    objeto_peliculas_cf  = PeliculasCiencia( nombre.lower(), puntuacion)
    
    if not objeto_peliculas_cf.nombre in dic_peliculas_cf.keys():
        dic_peliculas_cf[objeto_peliculas_cf.nombre] = objeto_peliculas_cf
      
        
    else:
        if objeto_peliculas_cf.nombre in dic_peliculas_cf.keys():
            print(objeto_peliculas_cf.nombre)

        print(speaker.Speak('Vale, tomo nota'))
    pausa()




class Titulos(CienciaFiccion,PeliculasCiencia,Custom):
    def __init__(self, titulo):
        self.titulo = titulo
        self.titulos = {}
    def __str__(self):

        return self.titulo

def agregar_titulo(titulos):

    titulo = input('Dime un titulo de una pelicula de ciencia ficción que te haya gustado:')
    
'''
