import main
import pygame
import ship
import random
import bullet


class Asteroid(object):
	def __init__(self, x, y, r):
		self.x = x
		self.y = y
		self.r = r
		self.dir = (random.random(), random.random())
		self.name = "asteroid"
		self.collision_rect = pygame.Rect(self.x-self.r,self.y, self.r, self.r)

	def draw(self):

		pygame.draw.rect(main.win, (0,0,0), self.collision_rect, 1)
		pygame.draw.circle(main.win, (255,255,255), (int(self.x),int(self.y)), int(self.r), 1)
		


	def move(self):
		self.x += self.dir[0] * 2
		self.y += self.dir[1] * 2
		self.collision_rect = pygame.Rect(self.x-self.r,self.y-self.r, self.r*2, self.r*2)

	def hasCollided(self, b):
		return self.collision_rect.colliderect(b.collision_rect)