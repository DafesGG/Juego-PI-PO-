import pygame
from pygame.sprite import Sprite
from pygame import *
import util

class Heroe(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.puntos = 0
		self.vida = 100
		self.imagenes = [util.cargar_imagen('imagenes/Car.png'),
						util.cargar_imagen('imagenes/Car_Fire.png'),
						util.cargar_imagen('imagenes/Car_Destroy.png')]
		self.image = self.imagenes[0]
		self.rect = self.image.get_rect()
		self.rect.move_ip(20, 200)
        
        
	def update(self):		
		
		teclas = pygame.key.get_pressed()
		if self.vida > 0:					
			
			if teclas[K_UP] and self.rect.y>100:
				self.rect.y -= 100
				self.image = self.imagenes[0]
				self.puntos = self.puntos + 1
				
			elif teclas[K_DOWN] and self.rect.y<300:
				self.rect.y += 100
				self.image = self.imagenes[0]
				self.puntos = self.puntos + 1
						
		else:
			self.image = self.imagenes[2]
