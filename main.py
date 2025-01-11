import pygame
from sys import exit
from space_ship import Space_ship
from bullet import Bullet
from meteorite import Meteorite
from random import randint
import time

W, H = 800, 600

pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Meteorite shooting")
clock = pygame.time.Clock()
bg = pygame.image.load("asset/background_stars.png").convert()
bg = pygame.transform.scale(bg, (W, H))
font_family_50 = pygame.font.Font("font/Pixeltype.ttf", 50)
font_family_120 = pygame.font.Font("font/Pixeltype.ttf", 120)
font_family_90 = pygame.font.Font("font/Pixeltype.ttf", 90)

ship = Space_ship()
Player = pygame.sprite.GroupSingle()
Player.add(ship)

Bullets = pygame.sprite.Group()
Bullets.add(Bullet(400, 300))

Meteorites = pygame.sprite.Group()

shoot = pygame.USEREVENT + 1
pygame.time.set_timer(shoot, 700)

spawn = pygame.USEREVENT + 2
pygame.time.set_timer(spawn, 1200)

meteorite_width = Meteorite(0, 0).width

game_active = True

game_start = False

count_destroyed = 0

# check collision
def check_collide():
	global count_destroyed
	for Bullet in Bullets:
		destroyed = pygame.sprite.spritecollide(Bullet, Meteorites, False)
		if destroyed: Bullet.kill()
		count_destroyed += len(destroyed)
		for destroyed_meteorite in destroyed:
			destroyed_meteorite.destroyed = True
	if pygame.sprite.spritecollide(Player.sprite, Meteorites, True):
		return False
	return True

# show current count of destroyed meteorites
def score_display(screen, count_destroyed):
	score_surf = font_family_50.render(f"Score : {count_destroyed}", False, 'WHITE')
	score_rect = score_surf.get_rect(topleft=(15, 15))
	screen.blit(score_surf, score_rect)

# main logic of the game
while True:
	if game_start:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			# spawn bullets and meteorites
			if game_active:
				if event.type == shoot:
					Bullets.add(Bullet(ship.rect.midtop[0], ship.rect.top))
				if event.type == spawn:
					Meteorites.add(Meteorite(randint(0, W - meteorite_width), 0))
			else:
				# reset game
				if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
					Bullets.empty()
					Meteorites.empty()
					Player.empty()
					count_destroyed = 0
					
					ship = Space_ship()
					Player.add(ship)
					game_active = True
					
		if game_active:
			screen.blit(bg, (0, 0))	
			
			Player.draw(screen)
			Player.update()
			
			Bullets.draw(screen)
			Bullets.update()
			
			Meteorites.draw(screen)
			Meteorites.update()
			
			score_display(screen, count_destroyed)
			
			game_active = check_collide()
		else:
			# restart menu
			screen.blit(bg, (0, 0))
			you_lose_surf = font_family_120.render(f"YOUR SCORE IS {count_destroyed}", True, 'WHITE')
			you_lose_rect = you_lose_surf.get_rect(center=(W//2, H//2))
			
			replay_surf = font_family_90.render("press R to replay", True, 'WHITE')
			replay_rect = replay_surf.get_rect(center=(W//2, H//2+70))
			
			screen.blit(you_lose_surf, you_lose_rect)
			screen.blit(replay_surf, replay_rect)
	else:
		
		# start menu
		screen.blit(bg, (0, 0))
		start_button_surf = pygame.image.load("asset/start_button.png").convert_alpha()
		start_button_rect = start_button_surf.get_rect(center=(W//2, H//2))
		screen.blit(start_button_surf, start_button_rect)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			if event.type == pygame.MOUSEBUTTONDOWN and start_button_rect.collidepoint(event.pos):
				game_start = True
		
	pygame.display.update()
	clock.tick(60)
	
pygame.quit()