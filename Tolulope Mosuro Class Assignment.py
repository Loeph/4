import math
class solids:
    def __init__(self,name,colour = "blue"):
        self.name= name
        self.colour= colour
        
    def solid_name(self):
        return self.name

    def solid_colour(self):
        return self.colour

class cylinder(solids):
    def __init__(self, radius, height):
        super().__init__(self)
        self.radius = radius
        self.height = height

    def cylinder_volume(self):
        return (math.pi* (self.radius)**2 * self.height)

class cuboid(solids):
    def __init__(self, length, breadth, height):
        super().__init__(self)
        self.length = length
        self.breadth = breadth
        self.height = height

    def cuboid_volume(self):
        return (self.length * self.breadth * self.height)

def poly_func(shape):
    shape.solid_colour()
    shape.solid_name()
    print (shape.solid_colour(), shape.solid_name())

d4 = solids("cuboid","Red")

x=solids("cylinder")
print("This is a ", x.solid_name())
a1 = cylinder(14, 30)
print("The colour is ", a1.solid_colour(), " with a volume of  ", a1.cylinder_volume())

x=solids("cuboid")
print("This is a ", x.solid_name())
b2 = cuboid(10, 5, 12)
print("The colour is ", b2.solid_colour(), " with a volume of  ", b2.cuboid_volume())

poly_func(d4)




    
