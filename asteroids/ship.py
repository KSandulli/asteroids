import pygame
import main
import math
import asteroid
import random


class Ship(object):
	def __init__(self, x, y):
		self.x1 = x
		self.y1 = y
		self.x2 = self.x1 - 10
		self.y2 = self.y1 - 25
		self.x3 = self.x1 + 10
		self.y3 = self.y1 - 25
		self.center = (((self.x1+self.x2+self.x3)/3),(self.y1+self.y2+self.y3)/3)
		self.vel = 0
		self.poly = [(self.x1,self.y1),(self.x2, self.y2), (self.x3, self.y3)]
		self.bullets = []
		self.dir = (0,0)
		self.name = "ship"
		self.collision_rect = pygame.Rect(self.center[0] -15, self.center[1] - 15,30,30)
		self.dontDraw = False


	def draw(self):
		pygame.draw.rect(main.win, (0,0,0,128), self.collision_rect, 1)
		if self.dontDraw:
			pygame.draw.polygon(main.win, (0,0,0), self.poly, 0)
			self.bullets = []
		else:
			pygame.draw.polygon(main.win, (255,255,255), self.poly, 0)

	def rotate(self, pts,cnt,ang):
	    theta = math.radians(ang)
	    c = math.cos(theta)
	    s = math.sin(theta)
	    rotatedPoly = []
	    """Rotating a point (x,y) about another point (x0,y0), by an angle θ (in radians), results in the point given by
		((x−x0)cosθ−(y−y0)sinθ+x0,(x−x0)sinθ+(y−y0)cosθ+y0)
		http://www.oxfordmathcenter.com/drupal7/node/83"""
	    for corner in pts:
	    	rotatedPoly.append(( ( (corner[0]-cnt[0])*c - (corner[1]-cnt[1])*s + cnt[0]),( (corner[0]-cnt[0])*s + (corner[1]-cnt[1])*c + cnt[1] ) ))
	    self.poly = rotatedPoly
	    self.x1 = self.poly[0][0]
	    self.x2 = self.poly[1][0]
	    self.x3 = self.poly[2][0]
	    self.y1 = self.poly[0][1]
	    self.y2 = self.poly[1][1]
	    self.y3 = self.poly[2][1]

	    self.collision_rect = pygame.Rect(self.center[0] -15, self.center[1] - 15,30,30)
	    return

	def move(self, dir):
		self.x1 += dir[0] * self.vel
		self.x2 += dir[0] * self.vel
		self.x3 += dir[0] * self.vel
		self.y1 += dir[1] * self.vel
		self.y2 += dir[1] * self.vel
		self.y3 += dir[1] * self.vel
		self.poly = [(self.x1,self.y1),(self.x2, self.y2), (self.x3, self.y3)]
		self.center = (((self.x1+self.x2+self.x3)/3),(self.y1+self.y2+self.y3)/3)

		self.collision_rect = pygame.Rect(self.center[0] -15, self.center[1] - 15,30,30)

	def getDir(self):
		x1 = self.poly[0][0]
		y1 = self.poly[0][1]
		ctr1 = self.center[0]
		ctr2 = self.center[1]

		radians = math.atan2(y1-ctr2,x1-ctr1)

		dx = math.cos(radians)
		dy = math.sin(radians)

		self.dir = (dx,dy)

		return (dx,dy)

	def hasCollided(self, a):
		return self.collision_rect.colliderect(a.collision_rect)

	def kill(self):
		self.dontDraw = True