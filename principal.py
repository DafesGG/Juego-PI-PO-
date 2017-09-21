import sys, pygame, util
from pygame.locals import *
from heroe import *
from villano import *
from random import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
ICON_SIZE = 52

def game():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )
    pygame.display.set_caption( "Juego del Carrito" )
    background_image = util.cargar_imagen('imagenes/fondo.jpg');
    pierde_vida = util.cargar_sonido('sonidos/pierde_vida.wav')
    inicio = util.cargar_sonido ('sonidos/inicio.wav')
    pygame.mouse.set_visible( False )
    temporizador = pygame.time.Clock()
    heroe = Heroe()
    inicio.play()
    villano = [(Villano((randint (450, 850),(120)),randint(10, 15))),
               Villano(((750),(220)),randint(10,15)),               
               Villano(((550),(300)),(20)),
               Villano((randint (450, 850),(120)),randint(5, 10)),
               Villano(((550),(300)),randint(10, 15))]
    
    while True:
        fuente = pygame.font.Font(None,35)
        texto_puntos = fuente.render("Puntos: "+str(heroe.puntos),1,(0,100,250))
        texto_vida = fuente.render("Vida: "+str(heroe.vida),1,(0,100,250))
        
        
        heroe.update()
        
        for n in villano:
			n.update()
            
        
        for n in villano:									
										
            if heroe.vida > 0 and heroe.rect.colliderect(n.rect):
                heroe.image = heroe.imagenes[1]
                pierde_vida.play()
                				
                if heroe.vida > 0:
                    heroe.vida=heroe.vida-1                   
                n.velocidad=randint(5, 15)		           
            
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(background_image, (0,0))
        screen.blit(heroe.image, heroe.rect)
        screen.blit(texto_vida,(400,450))
        screen.blit(texto_puntos,(100,450))
        for n in villano:
            screen.blit(n.image, n.rect)
        pygame.display.update()
        pygame.time.delay(55)

      
if __name__ == '__main__':
      game()

