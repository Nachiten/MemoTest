import pygame


def actualizarContadorPuntos():
    # create a font object.
    # 1st parameter is the font file
    # which is present in pygame.
    # 2nd parameter is size of the font
    font = pygame.font.Font('freesansbold.ttf', 22)

    # create a text suface object,
    # on which text is drawn on it.
    textoPuntos = font.render('Cantidad Puntos: ' + str(int(puntos)) + '/' + str(int(totalPuntos)), True,
                              (255, 255, 255), (0, 0, 0))

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

        textoReiniciar = font.render('HAS GANADO!!!', True, (255, 255, 255), (0, 0, 0))

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

    colorTexto = (255, 255, 255)
    colorFondo = colorCelda

    # create a text suface object,
    # on which text is drawn on it.
    textoPuntos = font.render(str(numeros[numFila][numCol]), True, colorTexto, colorFondo)

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
                dibujarRectangulo((0, 0, 0), numCol, numFila)


pygame.init()

# Comienza ejecucion

# Variables Importantes [Globales]
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
cantFilas = 4  # Default 60 # fixear problema con rectangulos
cantColumnas = 4

if cantFilas * cantColumnas / 2 % 2 != 0:
    print("Debe haber un numero par de casillas!!!")
    exit(-69)

# Configuracion
anchoVentana = 700  # Default 900x900
altoVentana = 700
segundosDelay = 1
run = True
estaEnPausa = True
colorCelda = (50, 50, 50)

pygame.display.set_caption("MemoTest")

matriz = [[0 for vx in range(cantFilas)] for vy in range(cantColumnas)]

'''
numeros = [[1, 2, 3, 4, 5, 6],
           [7, 8, 9, 10, 11, 12],
           [13, 14, 15, 16, 17, 18],
           [1, 2, 3, 4, 5, 6],
           [7, 8, 9, 10, 11, 12],
           [13, 14, 15, 16, 17, 18]]

numerosMostrados = [[1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1]]
'''

numeros = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [1, 2, 3, 4],
           [5, 6, 7, 8]]

numerosMostrados = [[1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1]]

# Estado: N = Nada Seleccionado, S = Selecciono algo
estado = "N"
posSeleccionada1 = (0, 0)
posSeleccionada2 = (0, 0)
puntos = 0
totalPuntos = (cantFilas * cantColumnas) / 2

# Setup Inicial
ventana = pygame.display.set_mode((anchoVentana, altoVentana))

pygame.display.update()

# leerArchivo()

# Bucle infinito
while run:
    mostrarMatriz()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            tocarCelda(pygame.mouse.get_pos())
            continue

    if estado == 'S1':
        dibujarNumeroEn(posSeleccionada1[0], posSeleccionada1[1])
    elif estado == 'S2':
        dibujarNumeroEn(posSeleccionada1[0], posSeleccionada1[1])
        dibujarNumeroEn(posSeleccionada2[0], posSeleccionada2[1])
        pygame.display.update()
        pygame.time.delay(1 * 1000)
        estado = 'N'

    actualizarContadorPuntos()

    # Actualizar display
    pygame.display.update()

    pygame.time.delay(segundosDelay * 100)

pygame.quit()
