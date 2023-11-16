import random

adivinanzas = [
    "¿Cuál es el animal que come con las patas?",
    "Blanca por dentro, verde por fuera. Si quieres que te lo diga, espera.",
    "¿Quieres té? ¡Pues toma té! ¿Sabes ya qué fruto es?",
    "Sobre una piel bien tensada, dos bailarines saltaban.",
    "solo cambia en un instante por una «efe» la «ge».",
    "El roer es mi trabajo, el queso mi aperitivo y el gato ha sido siempre mi más temido enemigo.",
    "Salta y salta, y la colita le falta.",
    "¿Cuál es el animal que come con las patas?",
    "Vuelo de noche, duermo de día y nunca verás plumas en ala mía.",
    "Dos ruedas, un sillín y un manillar. Si subes sobre ella te hará sudar",
    "Encima de la cabeza gira mi gran abanico y en la punta de la cola gira otro pequeñito.",
    "Mi misión es transportar y en la parada debo parar. Vengo de muchos colores, pero si te llevo a la escuela, mi color es amarillo. Llevo a la familia y a su equipaje. Paso todas las noches en el garaje. ¿Quién soy?",
    "Por un camino de hierro voy corriendo muy veloz, doy un fuerte silbido cuando llego a la estación. ¿Quién soy?",
    "Soy pájaro sin nido con las alas de metal, las ruedas tengo de goma y los ojitos de cristal.",
    "Cien amigos tengo, todos en una tabla, si yo no los toco, ellos no me hablan.",
    "Soy pequeño y de madera, tengo un arco y no flecha. Me pones entre hombro y barbilla y mi música es una maravilla.",
    "Siempre mirando al sol y no soy un caracol. Giro y giro sin fin y no soy un bailarín.",
    "En la tierra te sembraron, las aves te desearon, cuando estuviste dorado los hombres te segaron.",
    "En una larga abertura tengo yo mi dentadura y luego que empiezo a hablar, todas mis piezas se mueven sin poderlas yo parar.",
    "Tengo un sonido tan suave que los bardos me reclamaban. Apoyada en el suelo firme todas mis cuerdas pulsaban.",
    "A pesar de no ser buque tengo cuerdas y atavíos, también tengo un regio puente, pero nunca he visto un río.",
    "Sobre una piel bien tensada, dos bailarines saltaban.",
    "Zumba que te zumba, se oye mi son, en las noches navideñas, hasta que aparece el sol.",
    "Con tan sólo cuatro cuerdas, que un arco pone en acción, esta caja melodiosa te alegrará el corazón.",
    "Redondo como la luna y blanco como la cal. Me hacen de leche… ¡y ya no te digo más!",
    "Me rascan continuamente de forma muy placentera, mi voz es muy bien timbrada y mi cuerpo de madera.",
    "Una vieja con un diente que llama a toda la gente.",
    "Soy una caja adornada con dos palos para sonar, y en la banda de la escuela, me puedes encontrar. ¿Qué soy?",
    "Choco me dice la gente, late mi corazón. El que no sepa mi nombre, es un gran tontorrón.",
    "Blanca por dentro, verde por fuera. Si quieres que te lo diga, espera."
]

respuestas = ["PATO", "PERA", "TOMATE", "TAMBOR", "ELEFANTE", "RATON", "RANA", "PATO", "MURCIELAGO",
              "BICICLETA", "HELICOPTERO", "CARRO", "TREN", "AVION", "PIANO", "VIOLIN", "GIRASOL", "TRIGO",
              "PIANO", "ARPA", "GUITARRA", "ZAMBOMBA", "VIOLIN", "PANDERETA", "QUESO", "GUITARRA", "CAMPANA",
              "TAMBOR", "CHOCOLATE", "PERA"]



Bidas = 10
while Bidas>0:
    indiceadivinanza = random.randint(0,len(adivinanzas) -1)
    adivinanza = adivinanzas[indiceadivinanza]
    Correcta = respuestas[indiceadivinanza]
    print("tienes" , Bidas)
    print('')
    print('')
    print(adivinanza)
    print('')
    respuesta = input('Ingresa tu respuesta a la adivinanza; ')
    if respuesta == 'nose':
        print('Estudia las adivinanzas')
    if respuesta == Correcta:
        print('Lo lograste')
        print('')
        print('')
        print('')
        print('________00000000000___________000000000000________')
        print('______00000000_____00000___000000_____0000000______')
        print('____0000000_____________000______________00000_____')
        print('___0000000_______________0_________________0000____')
        print('__000000____________________________________0000___')
        print('__00000_____________________________________ 0000__')
        print('_00000______________________________________00000__')
        print('_00000_____________________________________000000__')
        print('__000000_________________________________0000000___')
        print('___0000000______________________________0000000____')
        print('_____ 000000____________________________000000______')
        print('_______000000________________________000000________')
        print('__________00000_____________________0000___________')
        print('_____________0000_________________0000_____________')
        print('_______________0000_____________000________________')
        print('_________________000_________000___________________')
        print('_________________ __000_____00_____________________')
        print('______________________00__00_______________________')
        del adivinanza[indiceadivinanza]
        del respuestas[Correcta]
            
    else:
     print('respuesta incorrecta intentalo nuevamente')
     
     print('──────┌┴┴┐───────')
     print('────╔═╡▀▀╞═╗─────')
     print('──────└╥╥┘───────')
     print('───────╝╚────────')
     Bidas = Bidas -1
    
if Bidas == 0:
 print('Te quedaste sin vidas intentalo otra vez')
elif not adivinanzas:
    print('Gramde Has responido todas')


        













