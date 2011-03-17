from math import pi, atan2, sqrt, cos, sin, fabs
from decimal import *
from decimal import Decimal as d

from pygame.locals import *

class SpaceSim:

    def __init__(self, SpaceObjects, G, timestep, maxstep, interface):
        self.SpaceObjects = SpaceObjects
        self.G = G
        self.timestep = timestep
        self.maxstep = maxstep
        self.interface = interface
        self.step = 0
        self.running = True
        getcontext().prec = 9

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
    
        primary_x_pos = primary.get_xpos()
        primary_y_pos = primary.get_ypos()
        primary_x_vel = primary.get_xvel()
        primary_y_vel = primary.get_yvel()
        primary_x_acc = 0.0
        primary_y_acc = 0.0
        primary_x_force = 0.0
        primary_y_force = 0.0
        primary_mass = primary.get_mass()
       

        #calculate and sum all accelerations
        for secondary in self.SpaceObjects:     

            if secondary != primary:
                
                secondary_x_pos = secondary.get_xpos()
                secondary_y_pos = secondary.get_ypos()

                secondary_mass = secondary.get_mass()
                secondary_radius = secondary.get_radius()
                                                                                
                theta = atan2((secondary_y_pos - primary_y_pos), (secondary_x_pos - primary_x_pos))
                F_p = d(str(self.G * (secondary_mass * primary_mass))) / ((secondary_y_pos - primary_y_pos)**2 + (secondary_x_pos - primary_x_pos)**2)

                
                primary_x_force = d(str(primary_x_force)) + (F_p * d(str(cos(theta))))
                primary_y_force = d(str(primary_y_force)) + (F_p * d(str(sin(theta))))



        primary_x_acc = (primary_x_force / d(str(primary_mass)))
        primary_y_acc = (primary_y_force / d(str(primary_mass)))
      
        #update variables in model
        primary.set_xacc(primary_x_acc)
        primary.set_yacc(primary_y_acc)

    #calculate velocities and positions            
    def __calcVelPos(self, primary):
    
        primary_x_pos = primary.get_xpos()
        primary_y_pos = primary.get_ypos()
        primary_x_vel = primary.get_xvel()
        primary_y_vel = primary.get_yvel()
        primary_x_acc = primary.get_xacc()
        primary_y_acc = primary.get_yacc()

        #x
        primary_x_vel_t = primary_x_vel + d(str(self.timestep)) * d(str(primary_x_acc)) 

        #todo: add runge-kutta integration
        primary_x_pos = primary_x_pos + self.timestep * (primary_x_vel + primary_x_vel_t)/ d('2.0')
        primary_x_vel = primary_x_vel_t

        #update variables in model
        primary.set_xvel(primary_x_vel)
        primary.set_xpos(primary_x_pos)
       
        #y
        primary_y_vel_t = primary_y_vel + d(str(self.timestep)) * d(str(primary_y_acc)) 
        primary_y_pos = primary_y_pos + self.timestep * (primary_y_vel + primary_y_vel_t)/d('2.0') 
        primary_y_vel = primary_y_vel_t

        #update variables in model
        primary.set_yvel(primary_y_vel)
        primary.set_ypos(primary_y_pos)

             
                     
                    
                         
