import pygame, pygame.gfxdraw
import sys
from pygame.locals import *
import time

class PygameInterface:

    def __init__(self, **kwargs):
    
        pygame.init()
        self.screen = pygame.display.set_mode((kwargs['window_size'][0], kwargs['window_size'][1]))
        
        pygame.display.set_caption("Space Sim")
        
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()

        self.background.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))

        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 20)
        self.clock = pygame.time.Clock()

        #camera stuff
        self.camera_width, self.camera_height = self.background.get_size()
        self.camera_center_x = kwargs['camera_center'][0]
        self.camera_center_y = kwargs['camera_center'][1]
        self.camera_zoom = kwargs['camera_zoom']
        self.camera_zoom_step = kwargs['camera_zoom_step']
        self.camera_scroll_step = kwargs['camera_scroll_step']
        
        #todo: add initial draw of objects
        pygame.display.flip()

       
        
    def update(self, SpaceObjects):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_EQUALS:
                    self.camera_zoom = self.camera_zoom * (1/self.camera_zoom_step)            
                if event.key == K_MINUS:
                    self.camera_zoom = self.camera_zoom * self.camera_zoom_step

                if event.mod == KMOD_LCTRL and event.key == K_UP:
                    self.camera_center_y = self.camera_center_y + self.camera_scroll_step * (1/self.camera_zoom)
                if event.mod== KMOD_LCTRL and event.key == K_DOWN:
                    self.camera_center_y = self.camera_center_y - self.camera_scroll_step * (1/self.camera_zoom)
                if event.mod == KMOD_LCTRL and event.key == K_LEFT:
                    self.camera_center_x = self.camera_center_x - self.camera_scroll_step * (1/self.camera_zoom)
                if event.mod == KMOD_LCTRL and event.key == K_RIGHT:
                    self.camera_center_x = self.camera_center_x + self.camera_scroll_step * (1/self.camera_zoom)
                       
        #update each objects position
        for obj in SpaceObjects:
            #calculate screen coordinates and scale changes
            screen_x = int(self.camera_width/2.0 + (obj.get_pos()[0] - self.camera_center_x) * self.camera_zoom)
            screen_y = int(self.camera_height/2.0 - (obj.get_pos()[1] - self.camera_center_y) * self.camera_zoom)
            screen_r = int(obj.get_radius() * self.camera_zoom)

            #draw object
            pygame.draw.circle(self.background, obj.get_color(), (screen_x, screen_y), screen_r, 0)

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
