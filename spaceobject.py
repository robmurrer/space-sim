#from decimal import Decimal as d

class SpaceObject:

    def __init__(self, name, mass, radius, xpos, ypos, xvel, yvel):

        self.name = name
        self.mass = mass
        self.radius = radius
        self.xpos = xpos
        self.xpos_t = 0
        self.ypos = ypos
        self.ypos_t = 0
        self.xvel = xvel
        self.xvel_t = 0
        self.yvel = yvel
        self.yvel_t = 0
        self.xacc = 0
        self.yacc = 0

    #doesn't work for some reason
    def __unicode__(self):
        return self.name + '\t' + str(self.xpos) + '\t' + str(self.ypos)
        
    def get_xpos(self):
        return self.xpos

    def get_ypos(self):
        return self.ypos

    #doesn't actually save must call .save()
    def set_xpos(self, new_xpos):
        self.xpos_t = new_xpos

    #doesn't actually save must call .save()
    def set_ypos(self, new_ypos):
        self.ypos_t = new_ypos

    def get_xvel(self):
        return self.xvel

    def get_yvel(self):
        return self.yvel
        
    #doesn't actually save must call .save()
    def set_xvel(self, new_xvel):
        self.xvel_t = new_xvel
        
    #doesn't actually save must call .save()
    def set_yvel(self, new_yvel):
        self.yvel_t = new_yvel      

    def get_xacc(self):
        return self.xacc

    def get_yacc(self):
        return self.yacc

    def set_xacc(self, new_xacc):
        self.xacc = new_xacc

    def set_yacc(self, new_yacc):
        self.yacc = new_yacc        

    def get_mass(self):
        return self.mass

    def get_name(self):
        return self.name

    def get_radius(self):
        return self.radius    

    #updates pos & vel with newer versions
    def save(self):
        self.xpos = self.xpos_t
        self.ypos = self.ypos_t
        self.xvel = self.xvel_t
        self.yvel = self.yvel_t


