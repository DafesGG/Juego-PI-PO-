import pygame
from pygame.sprite import Sprite
from pygame import *
import util

class Villano(Sprite):
	def __init__(self,coord,vel):
		Sprite.__init__(self)
		self.image = util.cargar_imagen('imagenes/Obstaculo.png')
		self.rect = self.image.get_rect()
		self.rect.move_ip(coord[0], coord[1])
		self.dir = "l"
		self.velocidad=vel
		self.puntos=0
        
	def update(self):
		
		tecla = pygame.key.get_pressed()
		if tecla [K_RIGHT]and self.velocidad<=100:
			self.velocidad+=1
		elif tecla [K_LEFT] and self.velocidad>1:
			self.velocidad-=1
				
		if self.dir == "l":
			self.rect.x -= self.velocidad
		elif self.dir == "l":
			self.rect.x += self.velocidad
		if self.rect.x<=0:
		
			self.rect.x = self.rect.x % 640

		if self.rect.x>=608:			
			self.dir="l"
		
			
