import pygame
from random import randint

class Meteorite(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		if randint(0, 2): 
			self.image = pygame.image.load("asset/meteor.png").convert_alpha()
			self.velocity = 3
		else: 
			self.image = pygame.image.load("asset/flaming_meteor.png").convert_alpha()
			self.velocity = 4
		self.image = pygame.transform.scale2x(self.image)
		
		self.explosion = pygame.image.load("asset/explosion.png").convert_alpha()
		self.count = 50
		
		self.destroyed = False
		
		self.rect = self.image.get_rect(topleft=(x, y))
		self.width = self.image.get_width()
	
	def destroy(self):
		if self.rect.top >= 600 or self.count == 0:
			self.kill()
		elif self.destroyed:
			if self.count == 50:
				self.image = self.explosion
				self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
			self.count -= 5
			self.velocity = 0
		
	def update(self):
		self.rect.y += self.velocity
		self.destroy()