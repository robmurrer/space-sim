#from decimal import Decimal as d

class SpaceObject:

    def __init__(self, **kwargs):

        self.name = kwargs['name']
        self.mass =  kwargs['mass']
        self.radius =  kwargs['radius']

        self.pos =  kwargs['pos']
        self.pos_t = (0,0)
       
        self.vel =  kwargs['vel']
        self.vel_t = (0,0)
 
        self.acc = (0,0)


        if not kwargs['color']:
            self.color = (255,255,255)
        else:
            self.color = kwargs['color']
            
    def get_pos(self):
        return self.pos

    def set_pos(self, new_pos):
        '''This only sets a temp variable.  Must call save() to complete update'''
        self.pos_t = new_pos

    def get_vel(self):
        return self.vel

    def set_vel(self, new_vel):
        '''This only sets a temp variable.  Must call save() to complete update'''
        self.vel_t = new_vel
        
    def get_acc(self):
        return self.acc

    def set_acc(self, new_acc):
        self.acc = new_acc   

    def get_mass(self):
        return self.mass

    def get_name(self):
        return self.name

    def get_radius(self):
        return self.radius    

    def save(self):
        '''copies the temporary variables to the real ones'''
        self.pos = self.pos_t
        self.vel = self.vel_t

    def get_color(self):
        return self.color


