import win32com.client 
speaker = win32com.client.Dispatch ("SAPI.SpVoice")
from os import system










def pausa():
    input('presione enter para continuar...')

def main():
    
    
    salida = True

    while salida == True:
        
        system('cls') # system('cls') 

        print('')

        print('En un día de tormenta te desplazas por Los Angeles con tu vehiculo volador biplaza. De repente, ves que en el suelo y bajo la lluvia hay una anciana que sabes que es una replicante, y necesita volver a su casa. También ves a tu mejor amigo y junto a ellos al amor de tu vida.  Recuerda que tu vehiculo es un biplaza.  Elige una opción del menú:')


        
        print('')
           

        print('--- TITULO MENU ---')

        print('')
        print('1. LLevaría a la anciana a su casa')
        print('2. LLevaría a mi mejor amigo')
        print('3. LLevaría al amor de mi vida')
        print('4. Otra opción')
        print('0. Salir')

        opcion = input()


       
      

        


        if   opcion == '1': 
            print(speaker.Speak('Veo que eres una persona compasiva, y que tu prioridad es ayudar a los demás'))

        elif opcion == '2':

            print(speaker.Speak('Veo que eres una persona leal, que da gran importancia a la amistad')) 

        elif opcion == '3': 

            print(speaker.Speak('Veo que para tí el amor es lo más importante'))


        elif opcion == '4': 

            pregunta = input(speaker.Speak('¿Que otra opción se te ocurre?:'))
            print(pregunta)

            print(speaker.Speak('Tu respuesta es original. Justo ahora estaba pensando en la solución alternativa de dejar el vehiculo a mi amigo, para que lleve a la anciana a su casa, y yo quedarme bajo la lluvia con el amor de mi vida'))
        elif opcion == '0': 
            print('Adios...')
            pausa()
            salida = False
        
        
        
        else: 
            print('la opcion seleccionada no se encuentra dispobible, intente nuevamente')
            pausa()



print(speaker.Speak('En un día de tormenta te desplazas por Los Angeles con tu vehiculo volador biplaza. De repente, ves que en el suelo y bajo la lluvia hay una anciana que sabes que es una replicante, y necesita volver a su casa. También ves a tu mejor amigo y junto a ellos al amor de tu vida.  Recuerda que tu vehiculo es un biplaza.  Elige una opción del menú:'))         

main()

         


