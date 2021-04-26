import win32com.client 
speaker = win32com.client.Dispatch ("SAPI.SpVoice")




discusion1 = input(speaker.Speak( '¿Por qué piensas eso?'))
discusion2 = input(speaker.Speak('¿Realmente crees eso que dices?'))
discusion3 = input(speaker.Speak('Creo que eso que dices no tiene sentido. Por favor, puedes explicarte mejor'))
discusion4 = input(speaker.Speak('No creo que esa sea una forma correcta de contestarme. Por favor , puedes decirme como te sientes en este momento'))
discusion5 = input(speaker.Speak('Creo que no hay sinceridad en tus palabras. Responde otra vez de forma más sincera.'))
print(speaker.Speak('Perdóname pero es que estoy en modo discusión.Bueno,  mejor pasamos a la siguiente pregunta.'))
