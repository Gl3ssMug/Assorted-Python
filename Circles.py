import math

class Circles():
    def __init__(self):
        pass
    
    def area(self, r):
        self.r = r
        print('area =',(2*math.pi*r))
    
    def circumference(self, r):
        self.r = r
        print('circumference =',(2*math.pi*r))
    
if __name__ == "__main__":
    cir = Circles()
    rad = float(input('input radius: '))
    cir.area(rad)
    cir.circumference(rad)



