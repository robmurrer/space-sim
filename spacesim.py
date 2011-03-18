from math import pi, atan2, sqrt, cos, sin, fabs
from pygame.locals import *

class SpaceSim:

    def __init__(self, **kwargs):
    
        self.SpaceObjects = kwargs['SpaceObjects']
        self.G = kwargs['G']
        self.maxstep = kwargs['maxstep']
        self.interface = kwargs['interface']

        
        self.step = 0
        self.running = True


    def run(self):
    
        while self.running:      
            self.update()
            self.interface.update(self.SpaceObjects)  

            if self.maxstep <= self.step:
                self.stop()
            self.step = self.step + 1

            
        self.interface.close()

    def stop(self):
        self.running = False
        
    def update(self):

        #calculate and sum accelerations/velocities
        for primary in self.SpaceObjects:
            self.__calcAcc(primary)

        #calculate positions
        for primary in self.SpaceObjects:
            self.__calcVelPos(primary)

        #make temporary variables permanant
        for primary in self.SpaceObjects:
            primary.save()


    #calculate and sum accelerations
    def __calcAcc(self, primary):
    
        primary_pos = primary.get_pos()
        primary_vel = primary.get_vel()
        primary_acc = (0.0, 0.0)
        primary_force = (0.0, 0.0)
        primary_mass = primary.get_mass()
       

        #calculate and sum all accelerations
        for secondary in self.SpaceObjects:     

            if secondary != primary:
                
                secondary_pos = secondary.get_pos()
                secondary_mass = secondary.get_mass()
                secondary_radius = secondary.get_radius()
                                                                                
                theta = atan2((secondary_pos[1] - primary_pos[1]), (secondary_pos[0] - primary_pos[0]))
                F_p = self.G * (secondary_mass * primary_mass) / ((secondary_pos[1] - primary_pos[1])**2 + (secondary_pos[0] - primary_pos[0])**2)
                
                primary_force = ((primary_force[0] + (F_p * cos(theta))), (primary_force[1] + (F_p * sin(theta))))

        primary_acc = ((primary_force[0] / primary_mass), (primary_force[1] / primary_mass))
      
        #update variables in model
        primary.set_acc(primary_acc)


    #calculate velocities and positions            
    def __calcVelPos(self, primary):
    
        primary_pos = primary.get_pos()

        primary_vel = primary.get_vel()

        primary_acc = primary.get_acc()

        
        primary_vel = ((primary_vel[0] + primary_acc[0]), (primary_vel[1] + primary_acc[1]))
        primary_pos = ((primary_pos[0] + primary_vel[0]), (primary_pos[1] + primary_vel[1]))

        #update variables in model
        primary.set_vel(primary_vel)
        primary.set_pos(primary_pos)

             
                     
                    
                         
