from spacesim import SpaceSim
from spaceobject import SpaceObject

from pygameinterface import PygameInterface


sun = SpaceObject(
    name ='moon',
    mass = 3e+8,
    radius = 1000,
    pos = (0,0),
    vel = (0, 0),
    color = (100, 100, 100),
)
    
earth = SpaceObject(
    name ='pluto',
    mass = 1e+8,
    radius = 1000,
    pos = (-1e+4, 0),
    vel = (0, 21.9e+1),
    color = (0, 100, 255),
)



    
SpaceObjects = [earth, sun]

interface = PygameInterface(
    window_size = (1100, 800),
    camera_center = (0, 0),
    camera_zoom = .01,
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

