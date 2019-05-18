import main
import pygame

class Bullet(object):
	def __init__(self, x, y, r, dir):
		self.x = x
		self.y = y
		self.r = r
		self.dir = dir
		self.name = "bullet"
		self.collision_rect = pygame.Rect(self.x-self.r,self.y-self.r, self.r*2, self.r*2)

	def draw(self):

		pygame.draw.rect(main.win, (0,0,0,128), self.collision_rect, 1)
		pygame.draw.circle(main.win, (255,255,255), (int(self.x),int(self.y)), int(self.r), 1)
		

	def move(self):
		self.x += self.dir[0] * 3
		self.y += self.dir[1] * 3
		self.collision_rect = pygame.Rect(self.x-self.r,self.y-self.r, self.r*2, self.r*2)