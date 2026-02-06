# ventana de juego
import pygame
import random

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
        self.rect = self.imagen.get_rect()
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

        self.sonido = pygame.mixer.Sound("cheer.wav")

    def mover(self):
        self.x += self.dir_x
        self.y += self.dir_y

    def rebotar(self):
        if self.x <= -self.ancho:
            self.reiniciar()
            self.puntuacion_ai += 1
        if self.x >= Wn_h:
            self.reiniciar()
            self.puntuacion += 1
        if self.y <= 0:
            self.dir_y = -self.dir_y
        if self.y + self.alto >= Wn_a:
            self.dir_y = -self.dir_y

    def reiniciar(self):
        self.x = Wn_h / 2 - self.ancho / 2
        self.y = Wn_a / 2 - self.alto / 2
        self.dir_x = -self.dir_x
        self.dir_y = random.choice([-4.5, 4.5])
        self.sonido.play()
        self.sonido.set_volume(0.2)


class RaquetaPong:
    def __init__(self):
        self.imagen = pygame.image.load("Barra.png").convert_alpha()
        # self.imagen1 = pygame.image.load("").convert_alpha()

        # dimensiones
        self.ancho, self.alto = self.imagen.get_size()

        # posicion de la raqueta
        self.x = 0
        self.y = Wn_a / 2 - self.alto / 2

        # direccion de movimiento
        self.dir_y = 0
        self.sonido = pygame.mixer.Sound("rebote.mp3")

    def mover(self):
        self.y += self.dir_y
        if self.y <= 0:
            self.y = 0
        if self.y + self.alto >= Wn_a:
            self.y = Wn_a - self.alto

    def mover_ia(self, pelota):
        if self.y > pelota.y:
            self.dir_y = -3
        elif self.y < pelota.y:
            self.dir_y = 3
        else:
            self.dir_y = 0

        self.y += self.dir_y

    def golpear(self, pelota):
        if self.x + self.ancho > pelota.x > self.x and pelota.y + pelota.alto > self.y and pelota.y < self.y + self.alto:
            pelota.dir_x = -pelota.dir_x
            pelota.x = self.x + self.ancho
            self.sonido.play()
            self.sonido.set_volume(0.25)


    def golpear_ia(self, pelota):
        if pelota.x + pelota.ancho > self.x and pelota.x < self.x + self.ancho and pelota.y + pelota.alto > self.y and pelota.y < self.y + self.alto:
            pelota.dir_x = -pelota.dir_x
            pelota.x = self.x - pelota.ancho
            self.sonido.play()
            self.sonido.set_volume(0.25)


class comodines(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.imagen = pygame.image.load("comodin.png")
        self.rect = self.imagen.get_rect()
        self.rect.x = random.randrange(Wn_h - self.rect.width)
        self.rect.y = random.randrange(Wn_a - self.rect.height)

    def destruir(self):
        self.kill()

class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, 0, 0, 1, 1)
    def update(self):
        self.left,self.top=pygame.mouse.get_pos()
class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen1, imagen2, x =300, y =300):
        self.imagen_nor=imagen1
        self.imagen_sel=imagen2
        self.imagen_act=self.imagen_nor
        self.rect= self.imagen_act.get_rect()
        self.rect.left, self.rect.top=(x,y)

    def update(self,pantalla,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_act = self.imagen_sel


        else: self.imagen_act = self.imagen_nor
        pantalla.blit(self.imagen_act, self.rect)

sprites = pygame.sprite.Group()
comodin_1 = comodines()
sprites.add(comodin_1)

def main():
    # inicializar pygame
    pygame.init()

    # inicializacion de la superficie de dibujo
    wn = pygame.display.set_mode((Wn_h, Wn_a))
    pygame.display.set_caption("Pong")

    # Fuente
    fuente = pygame.font.Font(None, 60)
    cursor1 = Cursor()
    pelota = Pelotapong("pelota.png")

    menuPrin = pygame.image.load("Menu.png").convert()
    mesa = pygame.image.load("Mesa.png").convert()
    menuFin = pygame.image.load("Fin.png").convert()

    ganador1 = pygame.image.load("Ganador1.png").convert_alpha()
    ganador2 = pygame.image.load("Ganador2.png").convert_alpha()


    bot1 = pygame.image.load("Jugador1_1.png")
    bot2 = pygame.image.load("Jugador1_2.png")
    #sprites boton 2 jugadores
    bot3 = pygame.image.load("2Jugadores_1.png")
    bot4 = pygame.image.load("2Jugadores_2.png")
    #sprites boton volver
    bot5 = pygame.image.load("Volver_1.png")
    bot6 = pygame.image.load("Volver_2.png")
    #sprites boton salir
    bot7 = pygame.image.load("Salir_1.png")
    bot8 = pygame.image.load("Salir_2.png")

    boton1 = Boton(bot1, bot2, 315, 300)
    boton2 = Boton(bot3, bot4, 315, 425)

    botonVolver = Boton(bot5,bot6, 315, 360)
    botonSalir = Boton(bot7, bot8, 315, 485)

    Raqueta_1 = RaquetaPong()
    Raqueta_1.x = 60

    Raqueta_2 = RaquetaPong()
    Raqueta_2.x = Wn_h - 60 - Raqueta_2.ancho

    pygame.mixer.music.load("CoolRide.mp3")
    select = pygame.mixer.Sound("select.wav")

    # Bucle principal
    jugando = True
    juegoAi = False
    menu = True
    fin = False
    juego2J = False

    while jugando:
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)
        for event in pygame.event.get():
            if event.type == QUIT:
                jugando = False
                pygame.quit()
        while menu:
            wn.blit(menuPrin, [0,0])
            cursor1.update()
            boton1.update(wn, cursor1)
            boton2.update(wn, cursor1)


            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
                    select.play()
                    select.set_volume(0.4)
                    if cursor1.colliderect(boton1.rect):

                        menu = False
                        juegoAi = True
                        jugando = True
                        fin = False
                        juego2J = False

                    elif cursor1.colliderect(boton2.rect):
                        juego2J = True
                        menu = False
                        fin = False
                        jugando = True
                        juegoAi = False

            pygame.display.update()

        while fin:

            wn.blit(menuFin, [0, 0])
            cursor1.update()
            botonVolver.update(wn, cursor1)
            botonSalir.update(wn, cursor1)

            if pelota.puntuacion == 7:
                    wn.blit(ganador1, (175, 125))
            elif pelota.puntuacion_ai == 7:
                    wn.blit(ganador2, (175, 125))

            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
                    select.play()
                    select.set_volume(0.4)
                    if cursor1.colliderect(botonVolver.rect):
                        pelota.puntuacion = 0
                        pelota.puntuacion_ai = 0
                        menu = True
                        fin = False
                        juegoAi = False
                        juego2J = False
                        jugando = True

                    elif cursor1.colliderect(botonSalir.rect):
                        jugando = False
                        menu = False
                        fin = False
                        juegoAi = False
                        juego2J = False


            pygame.display.update()

        while juegoAi:
            if pelota.puntuacion == 7 or pelota.puntuacion_ai == 7:
                fin = True
                menu = False
                juegoAi = False
                juego2J = False
                jugando = True



            pelota.mover()
            pelota.rebotar()
            Raqueta_1.mover()
            Raqueta_2.mover_ia(pelota)
            Raqueta_1.golpear(pelota)
            Raqueta_2.golpear_ia(pelota)



            wn.blit(mesa, [0,0])
            wn.blit(pelota.imagen, (pelota.x, pelota.y))
            wn.blit(Raqueta_1.imagen, (Raqueta_1.x, Raqueta_1.y))
            wn.blit(Raqueta_2.imagen, (Raqueta_2.x, Raqueta_2.y))


            texto = f"{pelota.puntuacion} : {pelota.puntuacion_ai}"
            letrero = fuente.render(texto, False, white)
            wn.blit(letrero, (Wn_h / 2 - fuente.size(texto)[0] / 2, 50))


            for event in pygame.event.get():

                    # Raqueta
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


            pygame.display.flip()
            pygame.time.Clock().tick(FPS)

        while juego2J:
            if pelota.puntuacion == 7 or pelota.puntuacion_ai == 7:
                fin = True
                menu = False
                juegoAi = False
                juego2J = False
                jugando = True


            pelota.mover()
            pelota.rebotar()
            Raqueta_1.mover()
            Raqueta_2.mover()
            Raqueta_1.golpear(pelota)
            Raqueta_2.golpear_ia(pelota)



            wn.blit(mesa, [0,0])
            wn.blit(pelota.imagen, (pelota.x, pelota.y))
            wn.blit(Raqueta_1.imagen, (Raqueta_1.x, Raqueta_1.y))
            wn.blit(Raqueta_2.imagen, (Raqueta_2.x, Raqueta_2.y))


            texto = f"{pelota.puntuacion} : {pelota.puntuacion_ai}"
            letrero = fuente.render(texto, False, white)
            wn.blit(letrero, (Wn_h / 2 - fuente.size(texto)[0] / 2, 50))


            for event in pygame.event.get():

                    # Raqueta
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


if __name__ == "__main__":
    main()
