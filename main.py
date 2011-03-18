from spacesim import SpaceSim
from spaceobject import SpaceObject

from pygameinterface import PygameInterface


sun = SpaceObject(
    name ='sun',
    mass = 80000,
    radius = 100,
    pos = (0,0),
    vel = (0,0),
    color = (255, 255, 0),
)
    
earth = SpaceObject(
    name ='earth',
    mass = 100,
    radius = 30,
    pos = (-1000, -2000),
    vel = (0, 6),
    color = (0, 100, 255),
)

mars = SpaceObject(
    name ='mars',
    mass = 100,
    radius = 30,
    pos = (1000, -1000),
    vel = (0, 6),
    color = (255, 20, 25),
)

pluto = SpaceObject(
    name ='pluto',
    mass = 30,
    radius = 5,
    pos = (0, 2000),
    vel = (-3, 0),
    color = (100, 100, 100),
)

moon = SpaceObject(
    name ='moon',
    mass = 45,
    radius = 10,
    pos = (1000, 1000),
    vel = (-2, 5),
    color = (220, 220, 220),
)
    
SpaceObjects = [earth, moon, sun, mars, pluto ]

interface = PygameInterface(
    window_size = (1100, 800),
    camera_center = (0, 0),
    camera_zoom = .07,
    camera_zoom_step = .9,
    camera_scroll_step = 200,

)


sim = SpaceSim(
    SpaceObjects = SpaceObjects, 
    G = 1,
    timestep =1,
    maxstep = 1e+40,
    interface=interface
)

sim.run()

