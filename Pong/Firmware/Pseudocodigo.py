# ventana de juego
importamos pygame
importamos random

de pygame.locals importamos salida

# Constantes para la superficie de dibujo
de pygame.sprite importamos AbstractGroup

Ancho ventana = 800  # Ancho de la ventana
Alto ventana = 600  # Alto de la ventana
Velocidad de refresco de la ventana = 60  # Fotogramas por segundo
Blanco = (255, 255, 255)  # Color del fondo de la ventana
Negro = (0, 0, 0)


clase Pelota:
    def inicializamos(self, referencia de imagen):
        # Atributos de la clase

        imagen de la pelota = pygame.imagen.cargar(referencia de imagen)
        cuadros de imagen = asignamos la imagen a los cuadros dibujados
        # dimensiones de la pelota
        ancho, alto = asignamos dimensiones a la imagen

        # Posicion de la pelota
        ubicacion en x = ancho de la ventana / 2 - ancho de la pelota / 2
        ubicacion en y = alto de la ventana / 2 - alto de la pelota / 2
        # Direccion y movimiento de la pelota
        direccion de la pelota en x = escoge una direccion al azar([-4.5, 4.5])
        direccion de la pelota en y = escoge una direccion al azar([-4.5, 4.5])

        # Puntuacion
        puntuacion jugador 1 = 0
        puntuacion jugador 2 = 0

    def mover(self):
        ubicacion en x += direccion en x
        ubicacion en y += direccion en y

    def rebotar(self):
        si ubicacion en x <= -ancho :
            reiniciar ubicacion
            puntuacion jugador 2 += 1
        si ubicacion en x >= ancho de ventana:
            reiniciar ubicacion
            puntuacion jugador 1 += 1
        si ubicacion en y <= 0:
            direccion en y = -direccion en y
        if ubicacion en y + alto de la pelota >= alto de la ventana:
            direccion en y = -direccion en y

    def reiniciar(self):
        ubicacion en x = ancho de la ventana / 2 - ancho de la pelota / 2
        ubicacion en y = alto de la ventana / 2 - alto de la pelota / 2
        direccion en x = -direccion en x
        direccion en y = escoger numero random([-4.5, 4.5])


clase Raqueta:
    def inicializamos(self):
        asignamos imagen = pygame.imagen.cargar("Barra.png").convert_alpha()
        # self.imagen1 = pygame.image.load("").convert_alpha()

        # dimensiones
        ancho de la raqueta, alto de la raqueta = asignamos las dimensiones

        # posicion de la raqueta
        posicion en x = 0
        posicion en y = alto de la ventana / 2 - alto de la raqueta / 2

        # direccion de movimiento
        direccion en y = 0

    def mover(self):
        ubicacion en y += direccion en y
        si ubicacion en y <= 0:
            ubicacion en y = 0
        si ubicacion en y + alto de la raqueta >= alto de la ventana:
            ubicacion en y = alto de la ventana - alto de la raqueta

    def mover_ia(self, pelota):
        si ubicacion raqueta en y > ubicacion pelota en y:
            direccion en y = -3
        o si ubicacion de la raqueta en y < ubicacion de la pelota en y:
            direccion en y = 3
        o :
            direccion de la raqueta en y = 0

        ubicacion en y += direccion en y

    def golpear(self, pelota):
        if ubicacion en x + ancho de la raqueta > ubicacion en x de la pelota > ubicacion en x de la raqueta and ubicacion en y de la pelota + alto de la pelota > ubicacion en y de la raqueta and ubicacion de la pelota en y < ubicacion de la raqueta en y + alto de la raqueta:
            direccion de la pelota en x = -direccion de la pelota en x
            ubicacion de la pelota en x = ubicacion de la raqueta en x + ancho de la raqueta

    def golpear_ia(self, pelota):
        if ubicacion en x + ancho de la raqueta > ubicacion en x de la pelota > ubicacion en x de la raqueta and ubicacion en y de la pelota + alto de la pelota > ubicacion en y de la raqueta and ubicacion de la pelota en y < ubicacion de la raqueta en y + alto de la raqueta:
            direccion de la pelota en x = -direccion de la pelota en x
            ubicacion de la pelota en x = ubicacion de la raqueta en x + ancho de la raqueta

clase Cursor(pygame.Rect):
    def inicializar(self):
        pygame.creamos el rectangulo.inicializar(self, 0, 0, 1, 1)

    def actualizar(self):
        dimension derecha, dimension posocion = pygame.obtener la posicion del mouse()


clase Boton(pygame.sprite.Sprite):
    def inicializar(asignar, imagen1, imagen2, x=300, y=300, *groups: AbstractGroup):
        super().inicializar(*groups)
        imagen_nor = imagen1
        imagen_sel = imagen2
        imagen_act = self.imagen_nor
        rect = self.imagen_act.get_rect()
        rect.left, self.rect.top = (x, y)

    def actualizar(self, pantalla, cursor):
        si cursor.ubicacion del cursol(self.rect):
            cambio de imagen
            self.imagen_act = self.imagen_sel
        o si:
            cambio de imagen
            self.imagen_act = self.imagen_nor
        dibujar imagen en la pantalla(self.imagen_act, self.rect)


sprites = pygame.sprite.Group()
comodin_1 = comodines()
sprites.add(comodin_1)


def main():
    # inicializar pygame
    pygame.init()

    # inicializacion de la superficie de dibujo
    ventana = pygame.display.set_mode((Wn_h, Wn_a))
    pygame.display.set_caption("Pong")

    # Fuente
    fuente = pygame.font.Font(None, 60)
    cursor1 = Cursor()
    pelota = Pelotapong("pelota.png")

    menuPrin = pygame.imagen.cargar("Menu.png").convert()
    mesa = pygame.imagen.cargar("Mesa.png").convert()
    menuFin = pygame.imagen.cargar("Fin.png").convert()

    ganador1 = pygame.imagen.cargar("Ganador1.png").convert_alpha()
    ganador2 = pygame.imagen.cargar("Ganador2.png").convert_alpha()

    bot1 = pygame.imagen.cargar("Jugador1_1.png")
    bot2 = pygame.imagen.cargar("Jugador1_2.png")
    # sprites boton 2 jugadores
    bot3 = pygame.imagen.cargar("2Jugadores_1.png")
    bot4 = pygame.imagen.cargar("2Jugadores_2.png")
    # sprites boton volver
    bot5 = pygame.imagen.cargar("Volver_1.png")
    bot6 = pygame.imagen.cargar("Volver_2.png")
    # sprites boton salir
    bot7 = pygame.imagen.cargar("Salir_1.png")
    bot8 = pygame.imagen.cargar("Salir_2.png")

    boton1 = Boton(bot1, bot2, 315, 300)
    boton2 = Boton(bot3, bot4, 315, 425)

    botonVolver = Boton(bot5, bot6, 315, 360)
    botonSalir = Boton(bot7, bot8, 315, 485)

    Raqueta_1 = Raqueta
    Raqueta_1.x = 60

    Raqueta_2 = Raqueta
    Raqueta_2.x = ancho de la ventana - 60 - Raqueta_2.ancho

    # Bucle principal
    jugando = True
    juegoAi = False
    menu = True
    fin = False
    juego2J = False

    mientras jugando sea True:

        mientras menu sea True:
            dibujar(menuPrin, [0, 0])
            actualizar cursor()
            actualizar boton 1(ventana, cursor1)
            actualizar boton 2(ventana, cursor1)

            para evento en pygame.event.get():
                si tipo de evento == salir:
                    jugando = False
                si evento tipo == pulsar el mpuse:
                    si ubicacion del cursor es el boton 1:
                        menu = False
                        juegoAi = True
                        jugando = True
                        fin = False
                        juego2J = False

                    o si ubicacion del cursor es el boton 2:
                        juego2J = True
                        menu = False
                        fin = False
                        jugando = True
                        juegoAi = False

            actualizar ventana ()

        mientras fin sea True:

            dibujar en la pantalla(menuFin, [0, 0])
            actualizar cursor()
            actualizar boton volver(ventana, cursor1)
            actualizar boton salir(ventana, cursor1)

            si pelota.puntuacion == 7:
                dibujar en la pantalla(ganador1, (175, 125))
            o si pelota.puntuacion_ai == 7:
                dibujar en la pantalla(ganador2, (175, 125))

            para evento in pygame.event.get():
                si evento tipo == presiona el mouse:
                    si la ubicacion del cursor es boton volver:
                        pelota.puntuacion = 0
                        pelota.puntuacion_ai = 0
                        menu = True
                        fin = False
                        juegoAi = False
                        juego2J = False
                        jugando = True

                    o si la ubicacion del cursor es boton salir:
                        jugando = False
                        menu = False
                        fin = False
                        juegoAi = False
                        juego2J = False

            pygame.actualizar pantalla()

        mientras juegoAi sea True:
            si puntuaciion jugador 1 == 7 o puntiacion jugador 2 == 7:
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

            dibujar en la pantalla(mesa, [0, 0])
            dibujar en la pantalla(pelota.imagen, (pelota.x, pelota.y))
            dibujar en la pantalla(Raqueta_1.imagen, (Raqueta_1.x, Raqueta_1.y))
            dibujar en la pantalla(Raqueta_2.imagen, (Raqueta_2.x, Raqueta_2.y))

            texto = f"{puntuacion del jugador 1} : {puntuacion del jugador 2}"
            letrero = renderizar fuente(texto, False, blanco)
            dibujar en la ventana(letrero, (ancho de la ventana / 2 - tamaño de la fuente(texto)[0] / 2, 50))

            para evento en pygame.event.get():
                si evento tipo == salir:
                    jugando = False

                    # Raqueta
                si evento tipo == oprimir tecla:
                    si oprime tecla == tecla w:
                        Raqueta_1 direccion en y = -5
                    si oprime tecla == tecla s:
                        Raqueta_1 direccion en y = +5

                si evento tipo == dejar de oprimir tecla:
                    si evento en la tecla == tecla w:
                        Raqueta_1 direccion en y = 0
                    si evento en la tecla == tecla s:
                        Raqueta_1 direccion en y = 0

            pygame.salto en display()
            pygame.time.Clock().tick(FPS)

        mientras juego2J sea True:
            si puntuacion jugador 1 == 7 or puntuacion jugador 2 == 7:
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

            dibujar en la ventana(mesa, [0, 0])
            dinujar en la ventana(pelota.imagen, (pelota.x, pelota.y))
            dibujar en la ventana(Raqueta_1.imagen, (Raqueta_1.x, Raqueta_1.y))
            dibujar en la ventana(Raqueta_2.imagen, (Raqueta_2.x, Raqueta_2.y))

            texto = f"{puntuacion jugador 1} : {puntuacion jugador 2}:
            letrero = renderizar fuente(texto, False, blanco)
            dibujar en la pantalla(letrero, (ancho de la ventana / 2 - tamaño de fuente(texto)[0] / 2, 50))

            para evento en pygame.event.get():
                si evento tipo == Salir:
                    jugando = False

                    # Raqueta
                si evento tipo == mantener presionado:
                    si evento en tecla == tecla w:
                        Raqueta_1 direccion en y = -5
                    si evento en la tecla == tecla s:
                        Raqueta_1 direccion en y = +5

                si evento tipo == soltar tecla:
                    si evento en tecla == tecla w:
                        Raqueta_1 direccion en y = 0
                    si evento en tecla == tecla s:
                        Raqueta_1 direccion en y = 0
                si evento tipo == presionar tecla:
                    si evento en tecla == tecla flecha arriba:
                        Raqueta_2 direccion en y = -5
                    si evento en tecla == tecla flecha abajo:
                        Raqueta_2 direccion en y = +5

                si evento tipo == soltar tecla:
                    si evento en tecla == tecla flecha arriba:
                        Raqueta_2 direccion en y = 0
                    si evento en tecla == tecla flecha abajo:
                        Raqueta_2 direccion en y = 0

            pygame.display.flip()
            pygame.time.Clock().tick(FPS)


if __name__ == "__main__":
    main()
