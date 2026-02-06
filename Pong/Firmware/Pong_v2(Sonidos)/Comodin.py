# ventana de juego
import random

import pygame
from pygame.locals import QUIT

# Constantes para la superficie de dibujo
Wn_h = 800  # Ancho de la ventana
Wn_a = 600  # Alto de la ventana
FPS = 60  # Fotogramas por segundo
white = (255, 255, 255)  # Color del fondo de la ventana
negro = (0, 0, 0)


class Pelotapong:
    def __init__(self, fichero_imagen):
        # Atributos de la clase

        self.imagen = pygame.image.load(fichero_imagen).convert_alpha()

        # dimensiones de la pelota
        self.ancho, self.alto = self.imagen.get_size()

        # Posicion de la pelota
        self.x = Wn_h / 2 - self.ancho / 2
        self.y = Wn_a / 2 - self.alto / 2

        # Direccion y movimiento de la pelota
        self.dir_x = random.choice([-4.5, 4.5])
        self.dir_y = random.choice([-4.5, 4.5])

        # Puntuacion
        self.puntuacion = 0
        self.puntuacion_ai = 0

    def mover(self):
        self.x += self.dir_x
        self.y += self.dir_y

    def rebotar(self):
        if self.x <= -self.ancho:
            self.reiniciar()
            self.puntuacion_ai += 1
            self.x += self.dir_x
            self.y += self.dir_y
        if self.x >= Wn_h:
            self.reiniciar()
            self.puntuacion += 1
            self.x += self.dir_x
            self.y += self.dir_y
        if self.y <= 0:
            self.dir_y = -self.dir_y
        if self.y + self.alto >= Wn_a:
            self.dir_y = -self.dir_y

    def reiniciar(self):
        self.x = Wn_h / 2 - self.ancho / 2
        self.y = Wn_a / 2 - self.alto / 2
        self.dir_x = -self.dir_x
        self.dir_y = random.choice([-4.5, 4.5])

class Comodin:
    def __init__(self):
        self.imagen = pygame.image.load("linea.png").convert_alpha()

        self.ancho, self.alto = self.imagen.get_size()

        self.x = random.choice([200, 600])
        self.y = random.choice([200, 500])

    def choque(self, pelota):
        if pelota.x + pelota.ancho > self.x and pelota.x < self.x + self.ancho and pelota.y + pelota.alto > self.y and pelota.y < self.y + self.alto:
            x = random.choice([1, 10])
            if x == 1: 
                pelota.dir_x = 15
                pelota.dir_y = 15
                if pelota.x <= -pelota.ancho or pelota.x >= Wn_h:
                    pelota.dir_x -= 15
                    pelota.dir_y -= 15
                    self.x = random.choice([200, 600])
                    self.y = random.choice([200, 500])


class RaquetaPong:
    def __init__(self):
        self.imagen = pygame.image.load("linea 1.png").convert_alpha()
        # self.imagen1 = pygame.image.load("").convert_alpha()

        # dimensiones
        self.ancho, self.alto = self.imagen.get_size()

        # posicion de la raqueta
        self.x = 0
        self.y = Wn_a / 2 - self.alto / 2

        # direccion de movimiento
        self.dir_y = 0

    def mover(self):
        self.y += self.dir_y
        if self.y <= 0:
            self.y = 0
        if self.y + self.alto >= Wn_a:
            self.y = Wn_a - self.alto

    def golpear(self, pelota):
        if self.x + self.ancho > pelota.x > self.x and pelota.y + pelota.alto > self.y and pelota.y < self.y + self.alto:
            pelota.dir_x = -pelota.dir_x
            pelota.x = self.x + self.ancho

    def golpear2(self, pelota):
        if pelota.x + pelota.ancho > self.x and pelota.x < self.x + self.ancho and pelota.y + pelota.alto > self.y and pelota.y < self.y + self.alto:
            pelota.dir_x = -pelota.dir_x
            pelota.x = self.x - pelota.ancho


def main():
    # inicializar pygame
    pygame.init()

    # inicializacion de la superficie de dibujo
    wn = pygame.display.set_mode((Wn_h, Wn_a))
    pygame.display.set_caption("Pong")

    # Fuente
    fuente = pygame.font.Font(None, 60)

    pelota = Pelotapong("pelota.png")

    Raqueta_1 = RaquetaPong()
    Raqueta_1.x = 60

    Raqueta_2 = RaquetaPong()
    Raqueta_2.x = Wn_h - 60 - Raqueta_2.ancho

    comodin = Comodin()

    # Bucle principal
    jugando = True

    while jugando:
        if pelota.puntuacion == 7 or pelota.puntuacion_ai == 7:
            jugando = False

        pelota.mover()
        pelota.rebotar()
        Raqueta_1.mover()
        Raqueta_2.mover()
        Raqueta_1.golpear(pelota)
        Raqueta_2.golpear2(pelota)
        comodin.choque(pelota)

        wn.fill(white)
        wn.blit(pelota.imagen, (pelota.x, pelota.y))
        wn.blit(Raqueta_1.imagen, (Raqueta_1.x, Raqueta_1.y))
        wn.blit(Raqueta_2.imagen, (Raqueta_2.x, Raqueta_2.y))
        wn.blit(comodin.imagen, (comodin.x, comodin.y))

        texto = f"{pelota.puntuacion} : {pelota.puntuacion_ai}"
        letrero = fuente.render(texto, False, negro)
        wn.blit(letrero, (Wn_h / 2 - fuente.size(texto)[0] / 2, 50))

        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False

            # Raqueta 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    Raqueta_1.dir_y = -5
                if event.key == pygame.K_s:
                    Raqueta_1.dir_y = +5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    Raqueta_1.dir_y = 0
                if event.key == pygame.K_s:
                    Raqueta_1.dir_y = 0

            # Raqueta 2
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    Raqueta_2.dir_y = -5
                if event.key == pygame.K_DOWN:
                    Raqueta_2.dir_y = +5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    Raqueta_2.dir_y = 0
                if event.key == pygame.K_DOWN:
                    Raqueta_2.dir_y = 0

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
