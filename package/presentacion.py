import win32com.client 
speaker = win32com.client.Dispatch ("SAPI.SpVoice")




print('                                               CHATBOT DE CINE                                      \n ')
print('                     Entrevista de 20 preguntas sobre la película Blade Runner de 1982. \n')
print (speaker.Speak(
'El presente proyecto consiste en  un programa conversacional estilo chatbot sobre la película Blade Runner de mil novecientos ochenta y dos. '
 
 'La interacción entre el chatbot y el usuario tendrá el formato de una'
'entrevista de 20 preguntas.'
 
 'Al terminar la entrevista el usuario deberá decidir si la conversación'
'se ha producido conmigo ,es decir,  con un programa conversacional(chatbot) o si en alguna o alguna de las preguntas intervino un ser humano real que ha simulado ser un chatbot.'
 
 
'  Sería conveniente,  antes de realizar la entrevista que el usuario haya visonado la película Blade Runner de mil novecientos ochenta y dos.'))







print(speaker.Speak( 'Comencemos la entrevista'))
