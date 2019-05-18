import pygame
import math
import ship
import bullet
import asteroid
import random

screenWidth = 500
screenHeight = 500
pygame.init()

win = pygame.display.set_mode((screenWidth,screenHeight))	
pygame.display.set_caption("Asteroids")



def mainLoop():

	playerDead = False
	

	asteroids = [asteroid.Asteroid(random.randrange(0,150), random.randrange(0,150), random.randrange(20,30)),
	asteroid.Asteroid(random.randrange(250,500), random.randrange(0,150), random.randrange(20,30)),
	asteroid.Asteroid(random.randrange(0,150), random.randrange(250,500), random.randrange(20,30)),
	asteroid.Asteroid(random.randrange(250,500), random.randrange(250,500), random.randrange(20,30))]

	prevTick = 0

	player = ship.Ship(screenWidth/2, screenHeight/2)

	run = True
	while run:

		pygame.time.delay(25)
		for event in pygame.event.get():
			if event.type == pygame.QUIT: run = False

		#player.checkKeys()

		keys = pygame.key.get_pressed()

		
		if keys[pygame.K_LEFT]:
			player.rotate(player.poly, player.center, -2)

		if keys[pygame.K_RIGHT]:
			player.rotate(player.poly, player.center, 2)

		if keys[pygame.K_UP]:
			player.vel += 0.05
			player.move(player.getDir())

		if not keys[pygame.K_UP]:
			if player.vel > 0:
				player.vel -= 0.03
				player.move(player.getDir())

		if keys[pygame.K_SPACE]:
			if pygame.time.get_ticks() - prevTick >= 650:
				player.bullets.append(bullet.Bullet(int(player.poly[0][0]), int(player.poly[0][1]), 2, player.getDir()))
				prevTick = pygame.time.get_ticks()


		if player.x2 > screenWidth and player.x3 > screenWidth:
			player.x1 -= 525
			player.x2 -= 525
			player.x3 -= 525

		if player.x2 < 0 and player.x3 < 0:
			player.x1 += 525
			player.x2 += 525
			player.x3 += 525

		if player.y2 > screenHeight and player.y3 > screenHeight:
			player.y1 -= 525
			player.y2 -= 525
			player.y3 -= 525

		if player.y2 < 0 and player.y3 < 0:
			player.y1 += 525
			player.y2 += 525
			player.y3 += 525
		
		win.fill((0,0,0))

		for b in player.bullets:
			b.draw()
			b.move()
			if b.x > screenWidth or b.y > screenHeight or b.x < 0 or b.y < 0: player.bullets.remove(b)
		for a in asteroids:
			if not playerDead:
				if player.hasCollided(a): 
					shipParts = [asteroid.Asteroid(player.x1, player.y1, random.randrange(5,10)),
					asteroid.Asteroid(player.x1, player.y1, random.randrange(5,10)),
					asteroid.Asteroid(player.x1, player.y1, random.randrange(5,10)),
					asteroid.Asteroid(player.x1, player.y1, random.randrange(5,10)),
					asteroid.Asteroid(player.x1, player.y1, random.randrange(5,10)),
					asteroid.Asteroid(player.x1, player.y1, random.randrange(5,10)),
					asteroid.Asteroid(player.x1, player.y1, random.randrange(5,10)),
					asteroid.Asteroid(player.x1, player.y1, random.randrange(5,10)),
					asteroid.Asteroid(player.x1, player.y1, random.randrange(5,10)),
					asteroid.Asteroid(player.x1, player.y1, random.randrange(5,10))]
					asteroids += shipParts
					player.kill()
					playerDead = True
			for b in player.bullets:
				if a.hasCollided(b):
					asteroids.remove(a)
					if a.r/2 > 5:
						newAsteroids = [asteroid.Asteroid(a.x,a.y,a.r/2),
						asteroid.Asteroid(a.x,a.y,a.r/2)]
					else: newAsteroids = []
					player.bullets.remove(b)
					asteroids += newAsteroids
			a.draw()
			a.move()
			if a.x > screenWidth: a.x -= 500
			if a.x < 0: a.x += 500
			if a.y > screenHeight: a.y -= 500
			if a.y < 0: a.y += 500
		
		if not player.dontDraw:
			player.draw()
		
		pygame.display.update()	

	pygame.quit()

if __name__ == "__main__":

	mainLoop()
