import pygame

class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.image.load("asset/laser.png").convert_alpha()
		self.image = pygame.transform.scale2x(self.image)
		self.rect = self.image.get_rect(midbottom=(x, y))
		self.velocity = 6
	
	def destroy(self):
		if self.rect.top <= 0:
			self.kill()
			
	def update(self):
		self.rect.y -= self.velocity
		self.destroy()
		