import pygame

class Space_ship(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("asset/ship_1.png").convert_alpha()
		self.image = pygame.transform.scale2x(self.image)
		self.rect = self.image.get_rect(midbottom=(400, 550))
		self.velocity = 6
	def move(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP] and self.rect.top - self.velocity > 0:
			self.rect.y -= self.velocity
		if keys[pygame.K_DOWN] and self.rect.bottom + self.velocity <= 600:
			self.rect.y += self.velocity
		if keys[pygame.K_LEFT] and self.rect.left - self.velocity > 0:
			self.rect.x -= self.velocity
		if keys[pygame.K_RIGHT] and self.rect.right + self.velocity <= 800:
			self.rect.x += self.velocity
	def update(self):
		self.move()
		
		
		