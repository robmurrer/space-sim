
class TestInterface:

    def __init__(self):
        print "Test Interface Loaded."
        print 'Name \t xpos \t ypos \t xvel \t yvel \t xacc \t yacc' 
    def update(self, SpaceObjects):
        for obj in SpaceObjects:
            print obj.get_name() + '\t' + str(obj.get_xpos()) + '\t' + str(obj.get_ypos()) + '\t' + str(obj.get_xvel()) + '\t' + str(obj.get_yvel()) + '\t' + str(obj.get_xacc()) + '\t' + str(obj.get_yacc())

    def close(self):
        print "Test Interface Closed."
