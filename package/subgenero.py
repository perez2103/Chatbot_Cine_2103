from os import system
import win32com.client 
speaker = win32com.client.Dispatch ("SAPI.SpVoice")

class Custom(object):

    def setattr_custom(self, atrib, valor):
        setattr(self, atrib, valor)

class CienciaFiccion:

    def __init__(self, nombre):
        self.nombre = nombre
        self.dic_peliculas_cf = {}
        self.titulos = {}

    def __str__(self):
        return self.nombre



class PeliculasCiencia(Custom):
    def __init__ (self, nombre, puntuacion):
        self.nombre = nombre
        self.puntuacion = puntuacion
        self.titulos = {}

    def __str__ (self):
        cadena = f'{self.nombre.lower()}'

        return cadena

      




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
    


    objeto_titulos_cf  = Titulos( titulo.lower())
    
    if not objeto_titulos_cf.titulo in titulos.keys():
        titulos[objeto_titulos_cf.titulo] = objeto_titulos_cf
      
        
    else:
        if objeto_titulos_cf.titulo in titulos.keys():
            print(objeto_titulos_cf.titulo)

        print(speaker.Speak('Vale, tomo nota'))
    


def leer(dic_peliculas_cf,titulos):
    
    for x in dic_peliculas_cf.values():
        print(x)
        for y in x.titulos.values():
            print(y)

    for x in titulos.values():
        print(x)
        for y in x.titulos.values():
            print(y)




pregunta = input('¿ En que subgenero de la ciencia ficción incluirias la pelicula BLADE RUNNER ?:')

obj_ciencia = CienciaFiccion('Ciencia y ficcion')
agregar_subgenero(obj_ciencia.dic_peliculas_cf)
agregar_subgenero(obj_ciencia.dic_peliculas_cf)
print(speaker.Speak('Te gustan los subgeneros de ciencia ficcion como'))
for i in obj_ciencia.dic_peliculas_cf:

    print(speaker.Speak(i))

print(speaker.Speak('A mi me gustan todos los subgeneros pero especialmente las peliculas sobre inteligencia artificial.  Pasemos a la siguiente pregunta.'))


'''
agregar_titulo(obj_ciencia.titulos)
agregar_titulo(obj_ciencia.titulos)
agregar_titulo(obj_ciencia.titulos)

print(speaker.Speak('Te gustan las peliculas'))
for i in obj_ciencia.titulos:
    print(speaker.Speak(i))
'''
'''
leer(obj_ciencia.titulos,obj_ciencia.dic_peliculas_cf)

'''




