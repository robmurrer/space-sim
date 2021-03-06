from math import pi, atan2, sqrt, cos, sin, fabs
import string

#G           = 6.67428e-11
G           = 1      #replaced to speed up the process
timestep    = .25    #time between movements
maxstep     = 10000 #to keep the program from running forever, until collision detection


planet_mass = 1000000
planet_x    = 0
planet_y    = 500

ship_mass   = 1

ship_i_x    = 0    #initial positions
ship_i_y    = 0

ship_i_x_v  = -3    #initial velocities
ship_i_y_v  = -2


ship_x, ship_y = ship_i_x, ship_i_y
ship_x_v, ship_y_v = ship_i_x_v, ship_i_y_v
step        = 0
outfile = open("output.txt", 'w')

while step != maxstep:

    theta = round(atan2((planet_y - ship_y), (planet_x - ship_x)))
   
    F_p = round(G * planet_mass * ship_mass / ((planet_y - ship_y)**2 + (planet_x - ship_x)**2))
    
    ship_f_x = round(F_p * cos(theta))
    ship_f_y = round(F_p * sin(theta))
    
    ship_x_a = round(ship_f_x / ship_mass)
    ship_y_a = round(ship_f_y / ship_mass)

    ship_x_v_t = round(ship_x_v + timestep * ship_x_a)
    ship_x = round(ship_x + timestep * (ship_x_v + ship_x_v_t)/2.0)
    ship_x_v = ship_x_v_t

    ship_y_v_t = round(ship_y_v + timestep * ship_y_a)
    ship_y = round(ship_y + timestep * (ship_y_v + ship_y_v_t)/2.0)
    ship_y_v = ship_y_v_t

   
    outfile.write(str(ship_x)+'\t'+str(ship_y)+'\n')
    
    step = step + 1

outfile.close()
