from abc import ABC

class Vec:
    def __init__(self, *args, shape=None):
        if len(args) == 0:
            if shape == None:
                raise Exception("Need coords or shape to initialize")
            
        if len(args) == 1:
            if type(args[0]) == list:
                args = args[0]
        self.ndims = len(args)
        self.coords = args
        if len(args) == 1:
            self.x = args
        elif len(args) == 2:
            self.x, self.y = args
        elif len(args) == 3:
            self.x, self.y, self.z = args
        elif len(args) == 4:
            self.w, self.x, self.y, self.z = args
    
    def __str__(self):
        return str(self.coords)


class ForceField(ABC):

    @abstractmethod
    def calculateForce(self, particle):
        pass

class Gravity(Field):
    def calculateForce(self, particle, particles):
        force = 
        for particle
class ElectricField(Field):
