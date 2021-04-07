import pygame
from funciones import crearInputBox
from funciones import crearBotonGuardar
from funciones import crearTextoInsertar
from funciones import mostrarMatriz
from funciones import actualizarContadores
from funciones import reaccionarAEstado
from funciones import manejarEventos
from funciones import llenarVentanaColorNegro
from funciones import setupInicialConTamanioActual
from funciones import juegoCorriendo

pygame.init()

setupInicialConTamanioActual()

# Bucle infinito
while juegoCorriendo():

    # Vaciar el fondo
    llenarVentanaColorNegro()

    # Crear textos y formas
    crearInputBox()
    crearBotonGuardar()
    crearTextoInsertar()

    # Mostrar la matriz inicial
    mostrarMatriz()

    # Manejar los eventos del sistema
    manejarEventos()

    # Actualizar los contadores
    actualizarContadores()

    # Reaccionar al estado actual
    reaccionarAEstado()

    # Actualizar display
    pygame.display.update()

    # Esperar para evitar espera activa
    pygame.time.delay(100)

pygame.quit()
