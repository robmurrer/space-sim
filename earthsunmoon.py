from spacesim import SpaceSim
from spaceobject import SpaceObject

from pygameinterface import PygameInterface


sun = SpaceObject(
    name ='sun',
    mass = 1.99e+30,
    radius = 6.96e+8,
    pos = (0,0),
    vel = (0,0),
    color = (255, 255, 0),
)
    
earth = SpaceObject(
    name ='earth',
    mass = 5.98e+24,
    radius = 6.37e+6,
    pos = (-1.5e+11, 0),
    vel = (0, 29.8e+8),
    color = (0, 100, 255),
)


moon = SpaceObject(
    name ='moon',
    mass = 7.36e+22,
    radius = 1.74e+6,
    pos = (-1.5e+11 + 3.82e+8, 0),
    vel = (0, 29.8e+8 + 990 ),
    color = (220, 220, 220),
)
    
SpaceObjects = [earth, moon, sun]

interface = PygameInterface(
    window_size = (1100, 800),
    camera_center = (0, 0),
    camera_zoom = .000000001,
    camera_zoom_step = .9,
    camera_scroll_step = 200,

)


sim = SpaceSim(
    SpaceObjects = SpaceObjects, 
    G = 1,
    maxstep = 1e+40,
    interface=interface
)

sim.run()

