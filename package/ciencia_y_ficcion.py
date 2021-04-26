import win32com.client 
speaker = win32com.client.Dispatch ("SAPI.SpVoice")

gustos_ficcion =[]

class Viajes_tiempo():
    def __init__ (self):
        print('Contesta: s/n)')
        self.var3 = input(speaker.Speak('¿Te gustó regreso al futuro?:'))
       
        if self.var3 == 's':
            gustos_ficcion.append('Regreso al futuro')
        else:
            print('vale')

class Scfy:

     def __init__ (self):

        print('Una pelicula de ciencia ficcion que te haya gustado:')

        self.var1=input(speaker.Speak(" Dime alguna pelicula de ciencia ficcion que te haya gustado?:"))
        gustos_ficcion.append(self.var1)
        print(' Contesta: s/n')
        self.var2=input(speaker.Speak("¿Te gustan las peliculas de viajes en el tiempo?:"))
        
        if self.var2 == 's':
            print(speaker.Speak('A mi tambien me gustan'))
            gustos_ficcion.append('viajes en el tiempo')
            
        else:
            print(speaker.Speak('Vale'))

ciencia = Scfy()

viaje_temporal = Viajes_tiempo()

print(speaker.Speak('Veo que te gusta'))
for i in gustos_ficcion:
    print(speaker.Speak(i))
if len(gustos_ficcion) == 3:
    print(speaker.Speak('Tenemos gustos parecidos. Esto parece el comienzo de una gran amistad'))
else:
    print(speaker.Speak('No coincidimos en nuestros gustos. '))







   



    
    












 

