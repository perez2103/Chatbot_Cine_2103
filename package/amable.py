import win32com.client 
speaker = win32com.client.Dispatch ("SAPI.SpVoice")



amable1 = input(speaker.Speak('Esa respuesta, aunque no lo parezca creo que es correcta. Por favor, respondeme con sinceridad.  ¿Piensas que nuestra entrevista transcurre con cordialidad?'))
print(speaker.Speak(' Yo pienso que es agradable conversar contigo. Por cierto recuerda que tus pensamientos y decisiones son lo que te hace ser lo que eres. Bien, pasemos a la siguiente pregunta'))


