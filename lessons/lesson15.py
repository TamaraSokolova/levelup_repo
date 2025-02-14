from main import 
import math
g=9.81
class B_calc:
    def __init__ (self, v, angle):
        self.angle
        self.v

    def D_(V, angle_g):
        angle= (3.14/180)*angle_g
        D=(V**2*math.sin(2*angle))/g
        return D
    
    def H_(V, angle_g):
        angle= (3.14/180)*angle_g
        H=(V**2*math.sin(angle**2))/2*g
        return H

    def T_(V, angle_g):
        angle= (3.14/180)*angle_g
        T=(2*V*math.sin(angle))/g
        return T

    a=D_(5,45)
    b=H_(7,77)
    c=T_(7,75)
    print('%.3f' %a)
    print('%.3f' %b)
    print('%.3f' %c)

    