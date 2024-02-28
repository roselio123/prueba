# se importan las libreria
import pygame
import pygame_menu

menu = pygame_menu.Menu('Welcome', 400, 300,
                       theme=pygame_menu.themes.THEME_BLUE)
menu.add_button('Play', main)
menu.add_button('About',
#space shooter beta
#controles:
#9: sube el volumen
#0: baja el volumen
#m: pone mute
#n: quita mute
#w: mueve hacia arriba
#a: mueve hacia la izquierda
#d: mueve hacia la derecha
#s: mueve hacia abajo
#c: dispara
                )
menu.add_button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)