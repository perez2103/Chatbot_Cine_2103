
from nltk.chat import Chat
from func_timeout import func_timeout



pares = [[
        r"(.*)salir|salir(.*)",
        ["Vale",]
    ],

    
    [

        r"mi nombre es(.*)|me llamo(.*)|soy(.*)",
        ["Hola , como estas ?",]
    ], 
    [

        r"(.*)musica(.*)|(.*)música(.*)|(.*)banda sonora(.*)",
        ["Vangelis",]
    ], 
    [

        r"(.*)autor(.*)|(.*)escritor(.*)|(.*)novelista(.*)",
        ["Philip K. Dick",]
    ], 
    [

        r"(.*)estreno(.*)|(.*)estrenó(.*)|(.*)salió(.*)",
        ["1982",]
    ], 
    [

        r"(.*)donde(.*)|(.*)transcurre(.*)|(.*)lugar(.*)",
        ["Los Angeles",]
    ], 
    [

        r"(.*)termina(.*)|(.*)final(.*)(.*)|desenlace(.*)",
        ["Deckard escapa con Rachel, final feliz",]
    ], 
     [

        r"(.*)Los Angeles(.*)|(.*)los angeles(.*)|(.*)ANGELES(.*)",
        ["2019",]
    ],
     [

        r"(.*)viven(.*)|(.*)vida(.*)|(.*)vive(.*)",
        ["Cuatro años",]
    ],
     [

        r"(.*)calificacion(.*)|(.*)calificación(.*)|(.*)calificar(.*)",
        ["Un 9",]
    ],
     [

        r"(.*)ciencia ficcion(.*)|(.*)ciencia ficción(.*)|(.*)Ciencia ficción(.*)",
        ["Me gusta mucho la Ciencia Ficción",]
    ],
    [

        r"(.*)Venezuela(.*)|(.*)venezuela(.*)",
        ["El cazador implacable",]
    ],
    [

        r"(.*)produccion(.*)|(.*)producción(.*)|(.*)productor(.*)",
        ["Michael Deeley, Ridley Scott y otros",]
    ],
    [

        r"(.*)guion (.*)|(.*)guión(.*)|(.*)Guion(.*)",
        ["Hamptin Fancher y otros",]
    ],
    [

        r"(.*)philip(.*)|(.*)Philip(.*)|(.*)Dick(.*)",
        ["¿Sueñan los androides con ovejas electricas?",]
    ],
    [

        r"(.*)fotografia(.*)|fotografía(.*)|(.*)Fotografía(.*)",
        ["Jordan Cronenweth",]
    ],
    [

        r"(.*)sonido(.*)|(.*)Sonido(.*)|(.*)sound(.*)",
        ["Peter Pennell y otro",]
    ],
    [

        r"(.*)montaje(.*)|(.*)Montaje(.*)(.*)|montador(.*)",
        ["Terry Rawlings y otro",]
    ],
    [

        r"(.*)vestuario(.*)|(.*)Vestuario(.*)|(.*)vestidos(.*)",
        ["Michal Kaplan y otro",]
    ],
    [

        r"(.*)efectos(.*)|(.*)especiales(.*)|(.*)Efectos(.*)",
        ["Douglas Trumbull y otro",]
    ],
    [

        r"(.*)pais(.*)|(.*)País(.*)|(.*)país(.*)",
        ["Estados Unidos",]
    ],
    [

        r"(.*)genero(.*)|(.*)Genero(.*)|(.*)subgenero(.*)",
        ["Ciencia ficción, subgenero distopías",]
    ],
    [

        r"(.*)duración(.*)|(.*)duracion(.*)|(.*)Duración(.*)|(.*)metraje(.*)|(.*)dura(.*)",
        ["117 minutos",]
    ],
    [

        r"(.*)recaudacion(.*)|(.*)Recaudación(.*)|(.*)recaudación(.*)|(.*)recaudo(.*)|(.*)recaudó(.*)",
        ["33.770.893 dolares",]
    ],
    [

        r"(.*)reparto(.*)|(.*)actores(.*)|interpretes(.*)",
        ["Harrison Ford,Ruter Hauer,Sean Young,Edwards James Olmos,Daryl Hannah",]
    ],
    [

        r"(.*)pris(.*)|(.*)Pris(.*)|priss(.*)",
        ["Daryl Hannah",]
    ],
    [

        r"(.*)Gaff(.*)|(.*)gaff(.*)|(.*)Gaf(.*)",
        ["Edwar James Olmos",]
    ],
    [

        r"(.*)roy(.*)|(.*)Roy(.*)|(.*)Roi(.*)",
        ["Rutger Hauer",]
    ],
    [

        r"(.*)Deckard(.*)|(.*)Rick(.*)|(.*)deckard(.*)",
        ["Harrison Ford",]
    ],
    [

        r"(.*)replicante(.*)|(.*)nexus(.*)|(.*)Replicante(.*)|(.*)replicantes(.*)",
        ["Androides identicos a los humanos, con limite de vida de 4 años y cognición empática",]
    ],
    
    [

        r"(.*)obra(.*)|(.*)novela(.*)|(.*)libro(.*)",
        ["¿Sueñan los androides con ovejas eléctricas ?",]
    ],
    [

        r"(.*)gusto(.*)|(.*)gustó(.*)(.*)|gusta(.*)",
        ["Toda la película me gusto mucho",]
    ],
    [

        r"(.*)zhora(.*)|(.*)Zhora(.*)|(.*)zora(.*)",
        ["Joana Cassidny",]
    ],
    [

        r"(.*)kowalski(.*)|(.*)Koalski(.*)|(.*)kovaski(.*)",
        ["Brion James",]
    ],
    [

        r"(.*)eres(.*)|(.*)inteligente(.*)",
        ["Yo no soy un replicante, soy un ser humano",]
    ],
    [

        r"(.*)ok(.*)|(.*)vale(.*)|(.*)bien(.*)",
        ["¿Todo bien en casa?",]
    ],
    [

        r"(.*)si(.*)",
        ["Vale",]
    ],
    [

        r"(.*)actriz(.*)|(.*)protagonista(.*)|(.*)guapa(.*)",
        ["Sean Young",]
    ],
    [

        r"(.*)humano(.*)|(.*)humanos(.*)|(.*)umano(.*)",
        ["Nos hace humanos el ser compasivos, el razonamiento, la creatividad, la autoconsciencia ...",]
    ],
    [

        r"(.*)aferran(.*)|(.*)aferrarse(.*)|(.*)recuerdos(.*)",
        ["Porque los aproximan a los humanos",]
    ],
    [

        r"(.*)palabras(.*)|(.*)tres(.*)|(.*)3(.*)",
        ["Pájaro,máquina y creo que coche",]
    ],
    [

        r"(.*)opinion(.*)|(.*)merece(.*)|(.*)piensas(.*)",
        ["Inteligente",]
    ],
    [

        r"(.*)monologo(.*)|(.*)monólogo(.*)|(.*)final(.*)",
        ["Magnifico el monólogo final del replicante Roy",]
    ],
    [

        r"(.*)test(.*)|(.*)tests(.*)|(.*)prueba(.*)",
        ["Pruebas a la que son sometidos los replicantes",]
    ],
    [

        r"(.*)trata(.*)|(.*)argumento(.*)|(.*)va(.*)",
        ["Deckard es un policía especializado en cazar replicantes, estos son seres artificiales. Los nexus 6 desarrollan emociones y cometen crímenes",]
    ],
    [

        r"(.*)escena(.*)|(.*)escenas(.*)|(.*)secuencia(.*)",
        ["Para mí la mejor secuencia es el monólogo final de Roy",]
    ],
    [
        r'(.*)nombre|(.*)como te llamas(.*)',
          ["Mejor al final de la entrevista.",]
    ],
    [
        r"(.*)como estas ?(.*)|(.*)bien y tu(.*)",
       ["Bien, y tu?",]
    ],
    [
        r"(.*)disculpa(.*)",
        ["No pasa nada",]
    ],
    [
        r"(.*)hola(.*)|(.*)hey(.*)|(.*)buenas",
        ["Hola", "Que tal",]
    ],
    [
        r"(.*)que(.*)|(.*)quieres ?(.*)",
        ["Nada gracias",]
        
    ],
    [
        r"(.*)creado(.*)|(.*)gracias(.*)",
        ["Fui creado por un ser humano",]
    ],
    [
        r"(.*)finalizar(.*)",
        ["Chao","Fue bueno hablar contigo"]
],
[
        r"(.*)novela|(.*)libro(.*)",
        ["sueñan los androides con ovejas electricas",]
    ],
     [
        r'(.*)director(.*)|(.*)dirigió(.*)|(.*)dirigio(.*)',
          ["Ridley Scott.",]
    ],
    [
        r"(.*)actor principal(.*)|(.*)protagonista(.*)",
       ["Harrison Ford",]
    ],
    [
        r"(.*)Deckard(.*)|(.*)bueno(.*)",
        ["Harrison Ford",]
    ],
    [
        r"(.*)Rachael(.*)|(.*)actriz principal(.*)|(.*)Rachel(.*)",
        ["Sean Young",]
    ],
    [
        r"(.*)Roy|(.*)malo",
        ["Rutger Hauer",]
        
    ],
    [
        r"(.*)año(.*)|(.*)estreno(.*)",
        ["1982",]
    ], 
    [
        r"(.*)musica(.*)|(.*)música(.*)|(.*)banda sonora(.*)",
        ["Vangelis",]
    ],
    [
        r"(.*)musica(.*)|(.*)banda sonora(.*)|(.*)música(.*)",
        ["Vangelis",]

    ],
[
        r"[A-z0-9!#$%&'*+/=?^_`{|}~-]",
        ["No entiendo.No puedo dar una respuesta a eso"]

    ],

]
def chatear():
    print('En esta ocasión se invierten los papeles.Serás tú el que haga las preguntas.\n')
    print(" Puedes preguntarme sobre mis conocimientos técnicos de la pelicula Blade Runner, por ejemplo director, actores, musica, etc.. \n")
    print ('Yo intentare responder a las preguntas que sepa.\n') #mensaje por defecto
    print('')
    print('RECUERDA:  DESPUÉS DE HACER 10 PREGUNTAS ESCRIBE " salir ".')
    print('')
    print('Puedes empezar:')
    chat = Chat(pares)
    chat.converse(quit='salir')
    #func_timeout(10.0,chat.converse)

chatear() 

print('')
print('Esto se esta acabando. Espero que te haya gustado el programa.')
