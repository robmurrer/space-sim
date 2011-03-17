import pygame, pygame.gfxdraw
import sys
from pygame.locals import *
import time

class PygameInterface:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1100, 800))
        pygame.display.set_caption("Space Sim")
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))

        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 20)
        self.clock = pygame.time.Clock()
        
        pygame.display.flip()

        #camera stuff
        self.camera_width, self.camera_height = self.background.get_size()
        self.camera_center_x = 400
        self.camera_center_y = 400
        self.camera_zoom = 1
        self.camera_zoom_step = .9
        self.camera_scroll_step = 200
        
    def update(self, SpaceObjects):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_EQUALS:
                    self.camera_zoom = self.camera_zoom * (1/self.camera_zoom_step)            
                if event.key == K_MINUS:
                    self.camera_zoom = self.camera_zoom * self.camera_zoom_step

                if event.key == K_UP:
                    self.camera_center_y = self.camera_center_y + self.camera_scroll_step * (1/self.camera_zoom)
                if event.key == K_DOWN:
                    self.camera_center_y = self.camera_center_y - self.camera_scroll_step * (1/self.camera_zoom)
                if event.key == K_LEFT:
                    self.camera_center_x = self.camera_center_x - self.camera_scroll_step * (1/self.camera_zoom)
                if event.key == K_RIGHT:
                    self.camera_center_x = self.camera_center_x + self.camera_scroll_step * (1/self.camera_zoom)
                       
        #update each objects position
        for obj in SpaceObjects:
            #calculate screen coordinates and scale changes
            screen_x = self.camera_width/2.0 + round((float(obj.get_xpos()) - self.camera_center_x) * self.camera_zoom)
            screen_y = self.camera_height/2.0 - round((float(obj.get_ypos()) - self.camera_center_y) * self.camera_zoom)
            screen_r = round(obj.get_radius() * self.camera_zoom)

            #draw object
            pygame.draw.circle(self.background, (250,250,250), (screen_x, screen_y), screen_r, 0)

            #update buffer    
            self.screen.blit(self.background, (0, 0))
            
        #wash background
        self.background.fill((0, 0, 0))

        #update fps
        self.clock.tick()
        text = self.font.render(str(int(self.clock.get_fps())) + "fps  |  center: (" + str(int(self.camera_center_x)) + ", " + str(int(self.camera_center_y)) + ")  |  zoom: " + str(round(self.camera_zoom, 8)), False, (255, 255, 255))
        self.screen.blit(text, text.get_rect(), text.get_rect())

        #refresh screen
        pygame.display.update()
        
    def debug(self, message):

        print message
              
    def close(self):

        pass
