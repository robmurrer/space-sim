import pygame, pygame.gfxdraw
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((1000, 800))



background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))



pygame.gfxdraw.circle(background, 100, 100, 10, (0, 0, 0))

screen.blit(background, (0, 0))
pygame.display.flip()


#input handling (somewhat boilerplate code):
while True: 
   for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
          sys.exit(0) 
      else: 
          print event
