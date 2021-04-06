import pygame
import random


def printearMatriz(unaMatriz):
    for unaFila in range(0, cantFilas):
        for unaColumna in range(0, cantColumnas):
            print(str(unaMatriz[unaFila][unaColumna]), end=', ')
            if unaMatriz[unaFila][unaColumna] < 10:
                print(' ', end='')
        print("")


def generarMatrizRandom():
    # Recorro la matriz numeros
    for unaFila in range(0, cantFilas):
        for unaColumna in range(0, cantColumnas):
            numeroCorrecto = False

            while not numeroCorrecto:
                filaRandom = random.randrange(0, cantFilas)
                columnaRandom = random.randrange(0, cantColumnas)

                if numerosAntesDeRandom[filaRandom][columnaRandom] != -1:
                    numeroCorrecto = True
                    numeros[unaFila][unaColumna] = numerosAntesDeRandom[filaRandom][columnaRandom]
                    numerosAntesDeRandom[filaRandom][columnaRandom] = -1

    # --- PASOS ---
    # 1 - Seleccionar numero random de matriz numerosAntesRandom
    # 2 - Si no fue seleccionado, tomarlo (si fue seleciconado, repetir desde paso 1)
    # 3 - Marcarlo como seleccionado


def setupInicial(cantFilasInput, cantColumnasInput):
    global numeros
    global numerosMostrados
    global numerosAntesDeRandom
    global estado
    global posSeleccionada1
    global posSeleccionada2
    global puntos
    global totalPuntos
    global user_text
    global cantFilas
    global cantColumnas
    global textoAEscribir

    resul = (cantFilasInput * cantColumnasInput / 2) % 2

    print(resul)
    if resul != 0:
        print("Debe haber un numero par de casillas!!!")
        textoAEscribir = '           La cantidad de casillas totales debe ser par!!           '
        estado = 'E'
        return

    cantFilas = cantFilasInput
    cantColumnas = cantColumnasInput

    # --- MATRICES ---
    numeros = [[0 for _ in range(cantColumnas)] for _ in range(cantFilas)]
    numerosAntesDeRandom = [[0 for _ in range(cantColumnas)] for _ in range(cantFilas)]
    numerosMostrados = [[0 for _ in range(cantColumnas)] for _ in range(cantFilas)]

    llenarMatrices()

    print("Numeros antes de random: ")
    printearMatriz(numerosAntesDeRandom)

    generarMatrizRandom()

    print("Numeros: ")
    printearMatriz(numeros)

    # --- ESTADO Y POS SELECCIONADAS ---
    # Estado: N = Nada Seleccionado, S1 = Selecciono un num, S2 = Selecciono 2 nums
    estado = "N"
    posSeleccionada1 = (0, 0)
    posSeleccionada2 = (0, 0)

    # --- PUNTOS ---
    puntos = 0
    totalPuntos = (cantFilas * cantColumnas) / 2

    user_text = ''

    # Actualizar display
    pygame.display.update()


posXBoton = 200
posYBoton = 650
anchoBoton = 100
altoBoton = 35


def crearBotonGuardar():
    pygame.draw.rect(ventana, colorBoton, (posXBoton, posYBoton, anchoBoton, altoBoton))

    font = pygame.font.Font('freesansbold.ttf', 18)
    textoBoton = font.render('Guardar', True, colorTexto, colorBoton)
    textRect = textoBoton.get_rect()
    textRect.center = (posXBoton + anchoBoton / 2, posYBoton + altoBoton / 2)
    ventana.blit(textoBoton, textRect)


def crearTextoInsertar():
    font = pygame.font.Font('freesansbold.ttf', 18)
    textoBoton = font.render(textoAEscribir, True, colorTexto, colorFondo)
    textRect = textoBoton.get_rect()
    textRect.center = (posXBoton + anchoBoton / 2, posYBoton - 80)
    ventana.blit(textoBoton, textRect)


def clickearBotonGuardar(unaPos):
    posX = unaPos[0]
    posY = unaPos[1]

    if posXBoton < posX < posXBoton + anchoBoton and posYBoton < posY < posYBoton + altoBoton:
        print("Clickeaste boton guardar")
        inputSeparado = user_text.split("x")
        print(inputSeparado[0] + " | " + inputSeparado[1])
        setupInicial(int(inputSeparado[0]), int(inputSeparado[1]))


def crearInputBox():
    base_font = pygame.font.Font(None, 32)

    posX = 200
    posY = posYBoton - 50

    input_rect = pygame.Rect(posX, posY, 100, 32)
    color = pygame.Color('lightskyblue3')

    pygame.draw.rect(ventana, color, input_rect, 3)
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    ventana.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    pygame.display.flip()


def reaccionarAEstado():
    global estado
    global textoAEscribir
    global user_text

    if estado == 'S1':
        dibujarNumeroEn(posSeleccionada1[0], posSeleccionada1[1])
    elif estado == 'S2':
        dibujarNumeroEn(posSeleccionada1[0], posSeleccionada1[1])
        dibujarNumeroEn(posSeleccionada2[0], posSeleccionada2[1])
        pygame.display.update()
        pygame.time.delay(1 * 1000)
        estado = 'N'
    elif estado == 'E':
        crearTextoInsertar()
        user_text = ''
        pygame.display.update()
        pygame.time.delay(3 * 1000)
        estado = 'N'
        textoAEscribir = 'Insertar el tamaño de la forma filasxcolumnas. Ej: 3x4'


def llenarMatrices():
    contador = 1

    for unaFila in range(0, cantFilas):
        for unaColumna in range(0, cantColumnas):
            numerosAntesDeRandom[unaFila][unaColumna] = contador
            numerosMostrados[unaFila][unaColumna] = 1
            contador += 1
            if contador > cantFilas * cantColumnas / 2:
                contador = 1


def actualizarContadorPuntos():
    # create a font object.
    # 1st parameter is the font file
    # which is present in pygame.
    # 2nd parameter is size of the font
    font = pygame.font.Font('freesansbold.ttf', 22)

    # create a text suface object,
    # on which text is drawn on it.
    textoPuntos = font.render('Cantidad Puntos: ' + str(int(puntos)) + '/' + str(int(totalPuntos)), True,
                              colorTexto, colorFondo)

    # create a rectangular object for the
    # text surface object
    textRect = textoPuntos.get_rect()

    # set the center of the rectangular object.
    textRect.center = (500, 20)

    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    ventana.blit(textoPuntos, textRect)

    if puntos == totalPuntos:
        font = pygame.font.Font('freesansbold.ttf', 40)

        textoReiniciar = font.render('HAS GANADO!!!', True, colorTexto, colorFondo)

        textRect2 = textoReiniciar.get_rect()
        textRect2.center = (anchoVentana - 250 + 53, 57)
        ventana.blit(textoReiniciar, textRect2)


def tocarCelda(unaPos):
    global estado
    global posSeleccionada1
    global posSeleccionada2
    global puntos

    posX = unaPos[0]
    posY = unaPos[1]

    for numFila in range(0, cantFilas):
        for numCol in range(0, cantColumnas):
            posXEsperada = x + numCol * (ancho + espacioX)
            posYEsperada = y + numFila * (alto + espacioY)
            if posXEsperada < posX < posXEsperada + ancho and \
                    posYEsperada < posY < posYEsperada + alto and \
                    numerosMostrados[numFila][numCol] == 1:
                print("Tocaste un cuadrado: Fila: " + str(numFila) + " Columna:" + str(numCol))
                if estado == 'N':
                    estado = 'S1'
                    posSeleccionada1 = (numFila, numCol)
                elif estado == 'S1':
                    if posSeleccionada1[0] == numFila and posSeleccionada1[1] == numCol:
                        return
                    if numeros[numFila][numCol] == numeros[posSeleccionada1[0]][posSeleccionada1[1]]:
                        print("Seleccionaste combinacion correcta")
                        puntos += 1
                        numerosMostrados[numFila][numCol] = 0
                        numerosMostrados[posSeleccionada1[0]][posSeleccionada1[1]] = 0
                    estado = 'S2'
                    posSeleccionada2 = (numFila, numCol)


def dibujarNumeroEn(numFila, numCol):
    # create a font object.
    # 1st parameter is the font file
    # which is present in pygame.
    # 2nd parameter is size of the font
    font = pygame.font.Font('freesansbold.ttf', 42)

    # create a text suface object,
    # on which text is drawn on it.
    textoPuntos = font.render(str(numeros[numFila][numCol]), True, colorTexto, colorCelda)

    # create a rectangular object for the
    # text surface object
    textRect = textoPuntos.get_rect()

    # set the center of the rectangular object.
    textRect.center = (x + numCol * (ancho + espacioX) + ancho / 2, y + numFila * (alto + espacioY) + alto / 2)

    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    ventana.blit(textoPuntos, textRect)


def dibujarNumeros():
    for numCol in range(0, cantColumnas):
        for numFila in range(0, cantFilas):
            # print("Fila: " + str(numFila) + " | Col: " + str(numCol))
            dibujarNumeroEn(numFila, numCol)


def dibujarRectangulo(colores, columna, fila):
    pygame.draw.rect(ventana,
                     colores,  # Color
                     (x + columna * (ancho + espacioX), y + fila * (alto + espacioY), ancho,
                      alto))  # posx, posy, ancho, alto


def mostrarMatriz():
    # Generar matriz de cuadrados
    for numFila in range(0, cantFilas):
        for numCol in range(0, cantColumnas):
            if numerosMostrados[numFila][numCol] == 1:
                dibujarRectangulo(colorCelda, numCol, numFila)
            else:
                dibujarRectangulo(colorFondo, numCol, numFila)


pygame.init()

# Comienza ejecucion

# Variables Importantes [Globales]
# --- BLOQUES ---
# Posicion Bloques
x = 20
y = 20
# Tamaño bloques
ancho = 50
alto = 50
# Espacio entre bloques
espacioX = 7
espacioY = 7

# Matriz
cantFilas = 6
cantColumnas = 6

# --- VENTANA ---
anchoVentana = 700
altoVentana = 700

# --- OTROS ---
segundosDelay = 1
run = True

# --- COLORES ---
colorCelda = (50, 50, 50)
colorTexto = (255, 255, 255)
colorFondo = (0, 0, 0)
colorBoton = (1, 111, 106)

# --- MATRICES ---
numeros = []
numerosMostrados = []
numerosAntesDeRandom = []

# --- ESTADO Y POS SELECCIONADAS ---
# Estado: N = Nada Seleccionado, S1 = Selecciono un num, S2 = Selecciono 2 nums
estado = "NULL"
posSeleccionada1 = (0, 0)
posSeleccionada2 = (0, 0)

# --- PUNTOS ---
puntos = 0
totalPuntos = 0

user_text = ''

# Setup de ventana
ventana = pygame.display.set_mode((anchoVentana, altoVentana))
ventana.fill(colorFondo)
pygame.display.set_caption("MemoTest")

textoAEscribir = 'Insertar el tamaño de la forma filasxcolumnas. Ej: 3x4'

setupInicial(cantFilas, cantColumnas)

# Bucle infinito
while run:

    ventana.fill(colorFondo)

    crearInputBox()
    crearBotonGuardar()
    crearTextoInsertar()

    mostrarMatriz()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            tocarCelda(pygame.mouse.get_pos())
            clickearBotonGuardar(pygame.mouse.get_pos())
            continue
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += evento.unicode

    actualizarContadorPuntos()

    reaccionarAEstado()

    # Actualizar display
    pygame.display.update()

    pygame.time.delay(segundosDelay * 100)

pygame.quit()
