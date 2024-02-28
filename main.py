# se importan las libreria
import pygame
# para poder manejar aleatoriedad
import random

# se define el tamñano de la ventana
ANCHO, ALTO = 750, 750
# velocidad
FPS = 30
NEGRO = (0, 0, 0)

# se crea lamcalse jugador
class Jugador(pygame.sprite.Sprite):
    # Sprite del jugador
    def __init__(self):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        # Rectángulo (jugador)
        self.image = pygame.image.load("images/spaceship.PNG")
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        # Centra el rectángulo (sprite)
        self.rect.center = (ANCHO // 2, ALTO // 2)
        # Velocidad inicial del personaje
        self.velocidad_x = 0
        self.velocidad_y = 0

    def update(self):
        # Velocidad predeterminada para que cuando no se pulse nada se quede quieto
        self.velocidad_x = 0
        self.velocidad_y = 0
        # Mantiene las teclas pulsadas
        teclas = pygame.key.get_pressed()
        # Mueve al personaje
        if teclas[pygame.K_a]:
            self.velocidad_x = -10
        if teclas[pygame.K_d]:
            self.velocidad_x = 10
        if teclas[pygame.K_w]:
            self.velocidad_y = -10
        if teclas[pygame.K_s]:
            self.velocidad_y = 10
        if teclas[pygame.K_c]:
            jugador.disparo()
        # Actualiza la velocidad del personaje.
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        # Limita el margen derecho
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
        # Limita el margen izquierdo
        if self.rect.left < 0:
            self.rect.left = 0
        # Limita el margen inferior
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO
        # Limita el margen superior
        if self.rect.top < 0:
            self.rect.top = 0

    #se crea la accion disparo dentro del personaje
    def disparo(self):
        bala = Disparos(self.rect.centerx, self.rect.top)
        balas.add(bala)

# se crea la clase enemigo
class Enemigo(pygame.sprite.Sprite):
    # Sprite del enemigo
    def __init__(self):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        # Rectángulo (enemigos)
        self.image = pygame.image.load("images/enemy.png")
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(ALTO - self.rect.height)
        # definimos velocidad
        self.velocidad_x = random.randrange(1, 5)
        self.velocidad_y = random.randrange(1, 5)

    def update(self):
        # actualiza la velocidad del enemigo
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        # Limita el margen izquierdo
        if self.rect.left < 0:
            self.velocidad_x += 1
        # Limita el margen derecho
        if self.rect.right > ANCHO:
            self.velocidad_x -= 1
        # Limita el margen inferior
        if self.rect.bottom > ALTO:
            self.velocidad_y -= 1
        # Limita el margen superior
        if self.rect.top < 0:
            self.velocidad_y += 1


class Lenemigo(pygame.sprite.Sprite):
    def __init__(self):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        # Rectángulo (enemigos)
        self.image = pygame.image.load("images/lenemy.png")
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(ALTO - self.rect.height)
        # definimos velocidad
        self.velocidad_x = random.randrange(1, 10)
        self.velocidad_y = random.randrange(1, 10)

    def update(self):
        # actualiza la velocidad del enemigo
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        # Limita el margen izquierdo
        if self.rect.left < 0:
            self.velocidad_x += 1
        # Limita el margen derecho
        if self.rect.right > ANCHO:
            self.velocidad_x -= 1
        # Limita el margen inferior
        if self.rect.bottom > ALTO:
            self.velocidad_y -= 1
        # Limita el margen superior
        if self.rect.top < 0:
            self.velocidad_y += 1


# se crea la clase bala
class Disparos(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("images/bang.png"), (10, 20))
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x

    def update(self):
            self.rect.y -= 25
            if self.rect.bottom < 0:
                self.kill()


# inicia el jeugo
pygame.init()

PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("sisas")
fondo = pygame.image.load("images/background.png").convert()
PANTALLA.blit(fondo, (0, 0))
clock = pygame.time.Clock()

# Grupo de sprites, instanciación del objeto jugador.
sprites = pygame.sprite.Group()
enemigos = pygame.sprite.Group()
lenemigos = pygame.sprite.Group()
balas = pygame.sprite.Group()
jugador1 = pygame.sprite.Group()

# el orden en que se carga indica cual superpone al otro, el segundo al primero
# enemigos
enemigo = Enemigo()
enemigos.add(enemigo)
for x in range(random.randrange(10)+1):
    lenemigo = Lenemigo()
    lenemigos.add(lenemigo)

# jugador
jugador = Jugador()
sprites.add(jugador)
jugador1.add(jugador)

# nombre e icono
pygame.display.set_caption('space shooter')
icono = pygame.image.load("images/logo.png")
pygame.display.set_icon(icono)

# se carga los datos de la musica
pygame.mixer.music.load('sound/space.ogg')
# bucle infinito
pygame.mixer.music.play(-1)
sonido = pygame.image.load('images/sound.png')
mute = pygame.image.load('Images/mute.png')
# max volumen
pygame.mixer.music.set_volume(0.5)

# Bucle de juego.
ejecutando = True
while ejecutando:
    # especificar velocidad
    clock.tick(FPS)
    # Cerrar Juego
    keys = pygame.key.get_pressed()

    # Control del audio
    # Baja volumen
    if keys[pygame.K_9] and pygame.mixer.music.get_volume() > 0.0:
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.01)
        PANTALLA.blit(sonido, (850, 25))
    elif keys[pygame.K_9] and pygame.mixer.music.get_volume() == 0.0:
        PANTALLA.blit(mute, (850, 25))
    # Sube volumen
    if keys[pygame.K_0] and pygame.mixer.music.get_volume() < 1.0:
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
        PANTALLA.blit(sonido, (850, 25))
    elif keys[pygame.K_0] and pygame.mixer.music.get_volume() == 1.0:
        PANTALLA.blit(sonido, (850, 25))
    # Desactivar sonido
    elif keys[pygame.K_m]:
        pygame.mixer.music.set_volume(0.0)
        PANTALLA.blit(mute, (850, 25))
    # Reactivar sonido
    elif keys[pygame.K_n]:
        pygame.mixer.music.set_volume(1.0)
        PANTALLA.blit(sonido, (850, 25))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False



    explosions = pygame.mixer.Sound('sound/explosion.ogg')
    collisions = pygame.sprite.groupcollide(enemigos, balas, False, True)
    lcollisions = pygame.sprite.groupcollide(lenemigos, balas, False, True)
    if collisions:
        enemigo.image = pygame.image.load("images/boom.png")
        enemigo.velocidad_y += 20
        explosions.play()
    elif enemigo.rect.top > ALTO:
        enemigo.kill()
    if lcollisions:
        lenemigo.image = pygame.image.load("images/boom.png")
        lenemigo.velocidad_y += 20
        explosions.play()
    elif lenemigo.rect.top > ALTO:
        lenemigo.kill()

    # Control de FPS
    # Actualización de sprites
    sprites.update()
    enemigos.update()
    balas.update()
    lenemigos.update()

    PANTALLA.blit(fondo, (0, 0))
    sprites.draw(PANTALLA)
    enemigos.draw(PANTALLA)
    balas.draw(PANTALLA)
    lenemigos.draw(PANTALLA)

    # actualizar pantalla
    pygame.display.flip()
pygame.quit()


# las imagenes y audios son de https://opengameart.org/
