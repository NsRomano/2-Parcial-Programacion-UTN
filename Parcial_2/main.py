from Package_Funciones.funciones import *

pygame.init()

ventana = pygame.display.set_mode(ventana_dimensiones)
pygame.display.set_caption("MILLONES | ¿Quien quiere ser millonario?")

logo = pygame.image.load("2repo\Parcial_2\imagenes\dolar.png")
pygame.display.set_icon(logo)
###########################################
while True:
    menu_juego,nombre_recibido = ventana_menu(ventana)
    if menu_juego == True:
        juego_continuar = ventana_de_juego(ventana,nombre_recibido)
        if juego_continuar == False:
            break
        elif juego_continuar == "GANADOR":
            retorno_ganador = ventana_ganador(ventana)
            if retorno_ganador == True:
                pantalla_puntos = ventana_score(ventana)
                if pantalla_puntos == False:
                    break
        elif juego_continuar == "RETIRADO":
            pantalla_puntos = ventana_score(ventana)
            if pantalla_puntos == False:
                break
    else:
        break
###########################################

pygame.quit()