from os import system
import win32com.client 
speaker = win32com.client.Dispatch ("SAPI.SpVoice")

import math

from package import presentacion


'''
PERFILES:


PERFIL CHATBOT: 

Modulo emocional.- El modulo emocional consiste en dos diccionarios, uno con palabras positivas
y otro con palabras negativas. Las palabras positivas o negativas se añaden a los diccionarios según la interacción
con el usuario. Cada palabra es una clave en el diccionario y tiene un valor de 1.

En un determinado momento se suman los valores de cada diccionario, y se procede a comparar el resultado.
Si los valores del diccionario nivel_agrado_ch  son iguales o superiores a los de nivel_desagrado_ch se
se imprime una frase, en caso contrario se imprime otra.


Corpus empatía.- 
Son dos listas, una sobre empatía y otra de falta de empatía.

Memoria.- 
Lista con frases que se incorporan a la memoria del chatbot.

Identidad.- 
Se incorporan datos propios del chatbot como nombre, edad, etc...


PERFIL USUARIO:

Información .-
Se recoge en listas y diccionarios la información que va suministrando el usuario.

'''
''' 
PERFIL CHATBOT
Modulo emocional 
'''
'''
'''
nivel_agrado_ch = {}
nivel_desagrado_ch = {}

corpus_empatia_ch = []
corpus_no_empatia_ch = []

'''Memoria'''
memoria_ch = []

'''Identidad'''
identidad_ch = []
nombre,edad,profesion = 'Lussy', 21, 'Asistente virtual'


''' PERFIL USUARIO

Informacion '''

caracteristicas_positivas_u = []
caracteristicas_negativas_u = []



'PREGUNTA Nº1'

print('\n PREGUNTA Nº 1 :')
print('')
print('Estas en un desierto, caminando por la arena, cuando de repente miras hacia abajo '
'y ves un galapago. El galapago yace sobre su espalda con el estomago cociendose al sol'
' y moviendo las patas para darse la vuelta.')

empatia = input ('\n ¿Lo ayudarías?:')

respuesta_afirmativa = ['si','pues si', 'lo ayudaría','sí', 'lo ayudaria', 'por supuesto', 'claro', 'claro que si','le daria la vuelta']

respuesta_negativa = ['no','nunca', 'no se', 'tal vez','no lo ayudaria', 'no lo ayudaría']


empatia = empatia.lower()

empatia = empatia.split()


r1 = empatia
r2 = ''
contador = 0

for i in r1 :
    while contador < 1:
        contador += 1
        if i in respuesta_afirmativa:
            print ('\n Creo que eres una persona empática')
            nivel_agrado_ch['empatica'] = 1
            caracteristicas_positivas_u.append('empática')
            corpus_empatia_ch.append('con empatía')
        elif i in respuesta_negativa:
            print('\n Creo que te falta empatia')
            nivel_desagrado_ch['poco empatica'] = 1
            caracteristicas_negativas_u.append('que debe mejorar su empatía')
            corpus_no_empatia_ch.append('que debe aumentar su compasión por los demás')
        else: 
            r2 = input('\n Por favor, contesta solo si o no, gracias:')
            r2 = r2.lower()
            r2 = r2.split()
            for i in r2:
                if i in respuesta_afirmativa:
                    print ('\n Creo que eres una persona empatica')
                    nivel_agrado_ch['empatica'] = 1
                    caracteristicas_positivas_u.append('empática')
                    corpus_empatia_ch.append('con empatía')
                elif i in respuesta_negativa:
                    print('\n Creo que debes mejorar tu empatia')
                    nivel_desagrado_ch['poco empatica'] = 1
                    caracteristicas_negativas_u.append('que debe mejorar su empatía')
                    corpus_no_empatia_ch.append('que debe aumentar su compasión por los demás')
                    break
                else:
                     break
               
print('\n Bueno, pues pasemos a la siguiente pregunta.')

print('')


'PREGUNTA Nº2'

print('PREGUNTA Nº2:')

print ('')
pocas_palabras = input('Podrías decirme en pocas palabras,  por qué los replicantes se aferran tanto a sus  recuerdos y fotografías:')

memoria_ch.append(pocas_palabras)

def contar(frases):
    fra=frases.split(".")
    for i in range(len(fra)):
        pals=len(fra[i].split(" "))
        return pals

x = contar(pocas_palabras)

if x >= 10 :
    print('\n Has usado màs de 10 palabras. Podrías sintetizar tu respuesta la próxima vez.Gracias.') 
else:
    print('\n Has usado menos de 10 palabras.Podrías extenderte un poco mas la próxima vez.Gracias')
print('') 
print('\n Juguemos un poco.Te digo tres palabras y tienes que recordarlas.') 
print ('Cuando transcurra un tiempo te preguntaré para ver si las recuerdas. ') 
print ('Las palabras son :  pájaro, máquina, coche.  ')
print('')            

amable = input('\n Por favor, contestame si o no. ¿ Crees que estoy siendo amable contigo ?:')

if pocas_palabras == amable:
    print(speaker.Speak('Parece que te gusta decir'))
    print(speaker.Speak(amable))
else:
    pass



amable = amable.lower()
amable = amable.split()
contador = 0
for i in amable:
     while contador < 1:
        contador += 1
        if i in respuesta_afirmativa:
            nivel_agrado_ch ['amable']= 1
            caracteristicas_positivas_u.append('comprensiva')
            corpus_empatia_ch.append('tolerante')

        elif i in respuesta_negativa:
            nivel_desagrado_ch['antipatica'] = 1
            caracteristicas_negativas_u.append('con poca paciencia')
            corpus_no_empatia_ch.append('insensible')
            break
        else:
            pass    
            

print('Vale .Pasemos a la siguiente pregunta.')
print('')



print('')

'PREGUNTA Nº3'

print('PREGUNTA Nº 3:')

from package import ser_humano

print(input('Dale a enter para continuar:'))

'PREGUNTA Nº4'

print('PREGUNTA Nº4')

amor = input('\n En la película se muestra una relación amorosa entre el protagonista y una replicante. \n'
'\n ¿ Crees que es posible el amor entre replicantes, o entre humanos y replicantes ? \n'
'\n Razona tu respuesta:')
memoria_ch.append(amor)

sentimiento_ch = input('\n Contesta solo si o no, ¿Te interesaría saber como me siento en este momento?')

sentimiento_cha = sentimiento_ch.lower()

if sentimiento_ch == 'si':
    nivel_agrado_ch['sensible']= 1
    caracteristicas_positivas_u.append('sensible')
else:
    nivel_desagrado_ch['insensible'] = 1
    caracteristicas_negativas_u.append('que no se conmueve facilmente')


'''
A continuación se suman los valores de cada diccionario, y se procede a comparar el resultado.
Si los valores del diccionario nivel_agrado_ch  son iguales o superiores a los de nivel_desagrado_ch se
se imprime una frase, en caso contrario se imprime otra.
'''

agrado1 = sum (nivel_agrado_ch.values())
agrado2 = sum (nivel_desagrado_ch.values())

if agrado1 >= agrado2 :
    print(speaker.Speak(' Pues me siento alegre. Me gusta conversar contigo.'))
else:
    print(speaker.Speak( 'Pues me siento triste.'))








' EL CHATBOT EVALUA EL PERFIL DEL USUARIO Y EL SUYO PROPIO'
   
try:
    u1 = caracteristicas_positivas_u[0]
except:
    print('')


try:
    u2 = caracteristicas_positivas_u[1]
except:
    print('')

try:
    ch1 = corpus_empatia_ch[0]
except:
    print()

try:    
    ch2 = corpus_empatia_ch[1]
except:
    print('')

try:    
    u3 = caracteristicas_negativas_u[0]
except:
    print('')

try: 
    u4 = caracteristicas_negativas_u[1]
except:
    print('')

try:
    u5 = caracteristicas_negativas_u[2]
except:
    print('')


print(speaker.Speak('En este momento puedo decirte que eres una persona'))
try:
    print(speaker.Speak(u1))
except:
    print()

try:
    print(speaker.Speak(u2))
except:
    print('')

try:
    print(speaker.Speak(u3))
except:
    print('')
try:
    print(speaker.Speak(u4))
except:
    print('')
try:
    print(speaker.Speak(u5))
except:
    print('')
print(speaker.Speak('En este momento yo me considero un ser inteligente'))

try:
    print(speaker.Speak(ch1))
except:
    print('')

try:
    print(speaker.Speak(ch2))
except:
     print('')






'PREGUNTA Nº5'

print('PREGUNTA Nº5:')

print('¿Te gustan las peliculas de ciencia ficción? s/n:')
x = input(speaker.Speak('¿Te gustan las peliculas de ciencia ficción?:'))
if x == 's':
    from package import ciencia_y_ficcion
else:
    print(speaker.Speak('Vale, continuemos la entrevista'))
       
print('')

from package import buho


print('')


'PREGUNTA Nº6:'
print('PREGUNTA Nº6:')

from package import subgenero

print('')

'PREGUNTA Nº7:'

print('PREGUNTA Nº7:')


from package import tormenta

print('')

'''
voy a intentar recordar las tres palabras que me dijiste. import buho2

'''

'PREGUNTA Nº8:'
print('PREGUNTA Nº8:')



e = 0


print('¿Que opinion te merece la replicante Rachel?:')
opinion = input(speaker.Speak('¿Que opinion te merece la replicante Rachel?:'))


print(speaker.Speak('Por favor, podrías decirme que opinas sobre mi.  Calificame de 0 a 10.  Muchas gracias'))
calificacion = input('Calificame de 0 a 10:')

try:
     entero = int(calificacion)
     if agrado1 > agrado2 and entero >= 7 :
         print(speaker.Speak(' Me has valorado positivamente, eso me hace sentir bien. Yo también estoy cogiendo un buen concepto de ti'))
         e = 1
     elif agrado1 < agrado2 and entero < 7:
         print(speaker.Speak( 'Creo que no me valoras lo suficiente, pero no importa eso no va a bajar mi autoestima'))
         e = -1
     else:
         print(speaker.Speak(' Estoy un poco confusa. Veo ciertas contradicciones en tus respuestas. Bueno, no pasa nada. Sigamos adelante.'))
     
    
	
except ValueError:
     print("Por favor, escribe un número entero")
     calificacion = input('Calificame de 0 a 10:')
     try:
         entero = int(calificacion)
         if agrado1 > agrado2 and entero >= 7 :
              print(speaker.Speak(' Me has valorado positivamente, eso me hace sentir bien. Yo también estoy cogiendo un buen concepto de ti'))
              e = 1
         elif agrado1 < agrado2 and entero < 7:
              print(speaker.Speak( 'Creo que no me valoras lo suficiente, pero no importa eso no va a bajar mi autoestima'))
              e = -1
         else:
              print(speaker.Speak(' Estoy un poco confusa. Veo ciertas contradicciones en tus respuestas. Bueno, no pasa nada. Sigamos adelante.'))
     
         
         
     except ValueError:
         print(speaker.Speak('Vale, pasemos a otra cosa'))

print('')

'PREGUNTA Nº9:'
print('PREGUNTA Nº9:')

print('¿Por qué crees que en toda la película no aparecen animales vivos?:')
animales_vivos = input(speaker.Speak('¿Por qué crees que en toda la película no aparecen animales vivos?:'))
if e == 1 :
    from package import amable

elif e == -1 :

    from package import discusion
    
else:
    print(speaker.Speak('Vale, pasemos a la siguiente pregunta'))



print('')
print('PREGUNTAS Nº 10 A 19 :')
print('')
print(speaker.Speak('\n En esta ocasión se invierten los papeles.Serás tú el que haga las preguntas.\n'))
print(speaker.Speak(" Puedes preguntar sobre  conocimientos técnicos de la pelicula Blade Runner, por ejemplo director, actores, musica, etc.. \n"))
print (speaker.Speak('Yo, o tal vez un humano intentaremos responder a las preguntas que formules.\n'))
print(speaker.Speak('RECUERDA: DESPUÉS DE HACER 10 PREGUNTAS DEBES ESCRIBIR " salir ".'))
print(speaker.Speak('Puedes empezar:'))



from package import conocimientos




print('PREGUNTA Nº 20:')

print(speaker.Speak('¿Durante la entrevista has estado conversando  exclusivamente con un chatbot o a veces era un humano y otras un chatbot?:'))
print(input('RESPUESTA ¿HUMANO ,CHATBOT, O HUMANO Y CHATBOT?:'))

print(speaker.Speak('Me llamo Lussy. Debo decirte que toda la entrevista la has realizado conmigo, es decir, con un chatbot. Algún día seré como los seres humanos, pero aún me falta mucho.'))
print(speaker.Speak('Durante la entrevista ha ido cambiando mi estado emocional, también he ido generando recuerdos,  por ejemplo,  recuerdo que a la pregunta numero 2 sobre por qué  los replicantes se aferran tanto a sus  recuerdos y fotografías, respondiste '))

print(speaker.Speak(memoria_ch[0]))

print(speaker.Speak('Supongo que cuando me incorporen machine learning avanzaré más en mi humanización. Ha sido un placer hablar contigo. Aquí finaliza este proyecto de fin de master de cice, la escuela profesional de nuevas tecnologías.'))

print(speaker.Speak( 'Este proyecto se ha desarrollado por el alumno Juan José Pérez Cervera. Ha sido profesor tutor del mismo Benjamín Peñaloza.'))
print(speaker.Speak( 'Hasta pronto.  Chao'))
