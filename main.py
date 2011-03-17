from spacesim import SpaceSim
from spaceobject import SpaceObject
from testinterface import TestInterface
from pygameinterface import PygameInterface

#SpaceObject(name, mass, radius, xpos, ypos, xvel, yvel)

#sun = SpaceObject('sun', 1000, 10, 200, 400, 0, 0)
earth = SpaceObject('earth', .01, 3, 400, 10000, 0, .4)
moon = SpaceObject('moon', .01, 2, 1000, 500, 1, -13)

#ship = SpaceObject('ship', .00001, 2, 800, 800, -1, .1)

#spaceobjects = [sun, earth, moon, ship]

rotmoon1 = SpaceObject('moon 1', 2, 2, 4000, 400, 0, 1)
sun = SpaceObject('sun', 100000, 100, 400, 400, 0, 0)
rotmoon2 = SpaceObject('moon 2', .75, 5, 3400, 400, 0, -3)
rotmoon3 = SpaceObject('moon 4', .35, 9, 1000, 400, 0, -13)

spaceobjects = [rotmoon1, rotmoon2, rotmoon3, sun, earth, moon]
interface = PygameInterface()

#SpaceSim(spaceobjects, gravity constant, timestep, maxstep, interface)
sim = SpaceSim(spaceobjects, 1, 1, 1e+40, interface)

sim.run()

