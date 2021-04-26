import win32com.client 
speaker = win32com.client.Dispatch ("SAPI.SpVoice")


print('Por favor, escribe aquí las tres palabras que te pedí que recordaras :')
print('')
buho = input(speaker.Speak('Estoy impaciente por saber si recuerdas las palabras que te dije. Por favor, podrías decirme las tres palabras que te pedí que recordaras.  Gracias'))
print(speaker.Speak('Las tres palabras eran pájaro, máquina y coche'))

'''
print('Por favor, ahora dime tú tres palabras y yo, pasado un tiempo, tendré que recordarlas. Escribe las tres palabras:')

buho2 =input(speaker.Speak('Por favor, ahora dime tú tres palabras y yo,  pasado un tiempo,  tendré que recordarlas. Escribe las tres palabras'))
'''