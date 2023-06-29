# code.Pylet - Direction and Distance
# watch the video here - https://youtu.be/DVYDkHdsTIM
# Any questions? Just ask!

import math, random, sys
import pygame
from pygame.locals import *

# exit the program
def events():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()


# define display surface			
W, H = 1024, 720
HW, HH = W / 2, H / 2
AREA = W * H

# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("code.Pylet - Direction and Distance")
FPS = 120

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

x, y 	 = HW, HH
pmx, pmy = x, y
dx, dy 	 = 0, 0
distance = 0
speed 	 = 3

# main loop
while True:
	events()

	m = pygame.mouse.get_pressed()
	if m[0] and not distance:
		mx, my = pygame.mouse.get_pos()
		
		radians = math.atan2(my - pmy, mx - pmx)
		distance = math.hypot(mx - pmx, my - pmy) / speed
		distance = int(distance)
		
		dx = math.cos(radians) * speed
		dy = math.sin(radians) * speed
		
		pmx, pmy = mx, my
		
	if distance:
		distance -= 1
		x += dx
		y += dy
	
	pygame.draw.circle(DS, WHITE, (int(x), int(y)), 25, 0)
	if distance:
		pygame.draw.circle( DS , ( 255 , 0 , 0 ) , ( pmx , pmy ) , 5, 0 ) 
	
	pygame.display.update()
	CLOCK.tick(FPS)
	DS.fill(BLACK)