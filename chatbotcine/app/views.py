from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.



'''
CHATBOT CINE

'''


def presentacion (request):
    datos = {}
    return render(request,'App/cine1.html', datos)






nivel_agrado_ch = {}
nivel_desagrado_ch = {}

corpus_empatia_ch = []
corpus_no_empatia_ch = []

'''Memoria'''
memoria_ch1 = []
memoria_ch2 = []
memo  = []
sentimientos = ['amar','enamorarse','amor']
'''Identidad'''
identidad_ch = []
nombre,edad,profesion = 'Lussy', 21, 'Asistente virtual'


''' PERFIL USUARIO

Informacion '''

caracteristicas_positivas_u = []
caracteristicas_negativas_u = []

respuesta_afirmativa = ['si','pues si', 'lo ayudaría','sí', 'lo ayudaria', 'por supuesto', 'claro', 'claro que si','le daria la vuelta']

respuesta_negativa = ['no','nunca', 'no se', 'tal vez','no lo ayudaria', 'no lo ayudaría']


'''
PREGUNTA Nº1

'''




def desierto (request):
    contador = 0
    empatica =''
    empatica2 =''
    falta_empatia = ''
    falta_empatia2= ''
    si_no = ''
    respuesta = ''
    respuesta2 =''
    if request.method == 'POST':
        respuesta = request.POST['algo']
        respuesta = respuesta.lower()
        respuesta = respuesta.split()
       


    for i in respuesta :
        
        while contador < 1:
            contador += 1
            if i in respuesta_afirmativa:
                empatica = ' Creo que eres una persona empática'
                nivel_agrado_ch['empática'] = 1
                caracteristicas_positivas_u.append('empática')
                corpus_empatia_ch.append('con empatía')
            elif i in respuesta_negativa:
                falta_empatia= 'Creo que te falta empatía'
                nivel_desagrado_ch['poco empatica'] = 1
                caracteristicas_negativas_u.append('que debe mejorar su empatía') 
                corpus_no_empatia_ch.append('que debe aumentar su compasión por los demás')

            else:
                si_no = 'Por favor, contesta solo sí o no , gracias'
                if request.method == 'POST':
                    respuesta2 = request.POST['algo']
                    respuesta2 = respuesta2.lower()
                    respuesta2 = respuesta2.split()
                for i in respuesta2:
                    if i in respuesta_afirmativa:
                        empatica2 = "Creo que eres una persona empática"
                        nivel_agrado_ch['empática'] = 1
                        caracteristicas_positivas_u.append('empática')
                        corpus_empatia_ch.append('con empatía')
                    elif i in respuesta_negativa:
                        falta_empatia2 = " Creo que debes mejorar tu empatía"
                        nivel_desagrado_ch['poco empática'] = 1
                        caracteristicas_negativas_u.append('que debe mejorar su empatía')
                        corpus_no_empatia_ch.append('que debe aumentar su compasión por los demás')
                        break
                    else:
                        break
   
   
   
   
   
   
    datos = { 'empatica': empatica, 'falta_empatia': falta_empatia, 'si_no':si_no, 'empatica2':empatica2, 'falta_empatia2':falta_empatia2 }    
    return render(request,'App/cine2.html', datos)
 


'''
PREGUNTA Nº2 

'''



def recuerdos (request):

    x = 0
    palabras1 =''
    palabras2 = ''
    respuesta3 =''
    
   

    if request.method == 'POST':
        respuesta3 = request.POST['algo']
        memoria_ch1.append(respuesta3)
    


    x = len(respuesta3)
    

    
    if x >= 10 :
        palabras1 = ' Has usado más de 10 palabras. Podrías sintetizar tu respuesta la próxima vez.Gracias.' 

        
    elif x > 0 :
        palabras2 = ' Has usado menos de 10 palabras.Podrías extenderte un poco mas la próxima vez.Gracias'
       
    else:
        pass


    datos = {'palabras1':palabras1, 'palabras2': palabras2}
    return render(request,'App/cine3.html', datos)
  

e = 0
def amor (request):
    e = 0
    contador = 0
    amor =''
    amor2 =''
    falta_amor = ''
    falta_amor2= ''
    si_no = ''
    respuesta = ''
    respuesta2 =''
    if request.method == 'POST':
        respuesta = request.POST['algo']
        respuesta = respuesta.lower()
        respuesta = respuesta.split()
       


    for i in respuesta :
        
        while contador < 1:
            contador += 1
            if i in respuesta_afirmativa:
                amor = 'Yo pienso igual que tú. Has hecho que me sienta alegre. Me gusta conversar contigo'
                e = 1
                
                
            elif i in respuesta_negativa:
                falta_amor= 'Siento que pienses así. Has hecho que me sienta triste.'
                e = -1
               
               

            else:
                si_no = 'Por favor, contesta solo sí o no , gracias'
                if request.method == 'POST':
                    respuesta2 = request.POST['algo']
                    respuesta2 = respuesta2.lower()
                    respuesta2 = respuesta2.split()
                for i in respuesta2:
                    if i in respuesta_afirmativa:
                        amor2 = "Yo pienso igual que tú. Has hecho que me sienta alegre. Me gusta conversar contigo"
                        e =1
                    elif i in respuesta_negativa:
                        falta_amor2 = " Siento que pienses así. Has hecho que me sienta triste."
                        e = -1
                        break
                    else:
                        break

    datos = {'amor':amor, 'amor2': amor2, 'falta_amor': falta_amor, 'falta_amor2': falta_amor2, 'si_no':si_no}
    return render(request,'App/cine4.html', datos)



def voz (request):
    datos = {}
    return render(request,'App/pruebavoz.html', datos)


x = ''
def rachel (request):
    x = ''
    datos = {'x':x}
    return render(request,'App/cine5.html', datos)

def rachel2 (request):
    x = 1
    datos = {'x':x}
    return render(request,'App/cine6.html', datos)

def rachel3 (request):
    x = 1
    datos = {'x':x}
    return render(request,'App/cine7.html', datos)

def tormenta (request):
    x = 1
    datos = {'x':x}
    return render(request,'App/cine8.html', datos)

def opcion1 (request):
    x = 1
    datos = {'x':x}
    return render(request,'App/cine9.html', datos)

def opcion2 (request):
    x = 1
    datos = {'x':x}
    return render(request,'App/cine10.html', datos)

def opcion3(request):
    x = 1
    datos = {'x':x}
    return render(request,'App/cine11.html', datos)

def opcion4 (request):
    opcion4 = ''
    respuesta4 = ''
    if request.method == 'POST':
        respuesta4 = request.POST['algo']
    x = len(respuesta4)
    if x >= 1 :
        opcion4 = 'Tu respuesta es original. Justo ahora estaba pensando en la solución alternativa de dejar el vehículo a mi amigo, para que lleve a la anciana a su casa, y yo quedarme bajo la lluvia con el amor de mi vida '
    else:
        pass    
   
    datos = {'opcion4':opcion4}
    
    return render(request,'App/cine12.html', datos)


def etica (request):

    contador = 0

    respuesta5 = ''
    respuesta6 =''
    etica =''
    etica2 =''
    no_etica =''
    no_etica2 = ''
    si_no =''
    
    
    if request.method == 'POST':
        respuesta5 = request.POST['algo']
        respuesta5 = respuesta5.lower()
        respuesta5 = respuesta5.split()
       


    for i in respuesta5 :
        
        while contador < 1:
            contador += 1
            if i in respuesta_afirmativa:
                etica = 'Estoy de acuerdo contigo.Pienso que las máquinas deberían tener criterios morales.'
               
                
                
            elif i in respuesta_negativa:
                no_etica= 'Discrepo de esa respuesta.Pienso que las máquinas deberían tener criterios morales.'
                
               
               

            else:
                si_no = 'Por favor, contesta solo sí o no , gracias'
                if request.method == 'POST':
                    respuesta6 = request.POST['algo']
                    respuesta6 = respuesta6.lower()
                    respuesta6 = respuesta6.split()
                for i in respuesta6:
                    if i in respuesta_afirmativa:
                        etica2 = "Estoy de acuerdo contigo.Pienso que las máquinas deberían tener criterios morales."
                        
                    elif i in respuesta_negativa:
                        no_etica2 = "Discrepo de esa respuesta.Pienso que las máquinas deberían tener criterios morales. "
                        
                        break
                    else:
                        break

    datos = {'etica':etica, 'etica2': etica2, 'no_etica': no_etica, 'no_etica2': no_etica2, 'si_no':si_no}
    return render(request,'App/cine13.html', datos)







def ser_humano(request):
    memo = ''
    respuesta8 = ''
    humano = ''
    if request.method == 'POST':
        respuesta8 = request.POST['algo']
        respuesta8 = respuesta8.lower()

        memoria_ch2.append(respuesta8)
        memo = memoria_ch2[0]
        

    if len(respuesta8) >= 1:
        humano = 'Es una respuesta interesante, pero tal vez se podría mejorar esa respuesta. Tu respuesta sino me equivoco ha sido esta:'
    else:
        pass
   
    datos = { 'humano':humano, 'respuesta8':respuesta8 ,'memo':memo}

    return render(request,'App/cine14.html', datos)


def fotos (request):
    
    tres = ''
    respuesta9 = ''
   
    if request.method == 'POST':
        respuesta9 = request.POST['algo']
        respuesta9 = respuesta9.lower()
       
        
        

    if len(respuesta9) >= 1:
        tres = 'Las tres mujeres han sido creadas por inteligencia artificial'
        pass
   
    datos = { 'tres':tres}

    return render(request,'App/cine15.html', datos) 



def test (request):

    
    
    compasiva1 = '' 
    compasiva2 ='' 
      
    compasiva3 =''
    compasiva4 = ''
    sentimientos =''
    contador = 0
    si_no = ''
    respuesta10 = ''
    respuesta11 =''
    if request.method == 'POST':
        respuesta10 = request.POST['algo']
        respuesta10 = respuesta10.lower()
        respuesta10 = respuesta10.split()
    for i in respuesta10 :
        while contador < 1:
            contador += 1
            if i in respuesta_afirmativa and len(caracteristicas_positivas_u) == 1 :
                compasiva1 = 'Tienes razón. Eres una persona compasiva, algo que es esencialmente humano'
                    
            elif i in respuesta_afirmativa and len(caracteristicas_positivas_u) == 0:
                compasiva2 = 'Dices que sí pasarías el test, pero veo que te falta mejorar tu empatía, algo que es propio de los seres humanos.'
            elif i in respuesta_negativa and len(caracteristicas_positivas_u) == 1 :
                compasiva3 = 'No entiendo porque piensas así, has demostrado en la entrevista que eres una persona compasiva, algo esencialmente humano'
            elif i in respuesta_negativa and len(caracteristicas_positivas_u) == 0 :
                compasiva4 = 'Es cierto que te falta mejorar tu empatía, pero eso no significa que no seas un ser humano.'
            else:
                si_no = 'Por favor, contesta solo sí o no , gracias'
                if request.method == 'POST':
                    respuesta11 = request.POST['algo']
                    respuesta11 = respuesta11.lower()
                    respuesta11 = respuesta11.split()
                for i in respuesta11:
                    if i in respuesta_afirmativa and len(caracteristicas_positivas_u) == 1 :
                        compasiva1 = 'Tienes razón. Eres una persona compasiva, algo que es esencialmente humano'
                    elif i in respuesta_afirmativa and len(caracteristicas_positivas_u) == 0:
                        compasiva2 = 'Dices que sí pasarías el test, pero veo que te falta mejorar tu empatía, algo que es propio de los seres humanos.'
                    elif i in respuesta_negativa and len(caracteristicas_positivas_u) == 1 :
                        compasiva3 = 'No entiendo porque piensas así, has demostrado en la entrevista que eres una persona compasiva, algo esencialmente humano'
                    elif i in respuesta_negativa and len(caracteristicas_positivas_u) == 0 :
                        compasiva4 = 'Es cierto que te falta mejorar tu empatía, pero eso no significa que no seas un ser humano.'
                        break
                    else:
                        break
    datos = { 'compasiva1': compasiva1, 'compasiva2': compasiva2, 'compasiva3':compasiva3, 'compasiva4':compasiva4 ,'si_no': si_no, 'sentimientos': sentimientos }   
    return render(request,'App/cine16.html', datos)
        



def fin (request):
    x = ''
    datos = {'x':x}
    return render(request,'App/cine17.html', datos)



def chatbot (request):
    datos = {}
    return render(request,'App/cine18.html', datos)