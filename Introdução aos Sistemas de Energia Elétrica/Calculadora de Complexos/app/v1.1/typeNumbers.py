from math import cos, sin, atan2, pi

class Graus:
    def __init__(self, graus):
        if graus >= 360:
            graus = graus % 360
        if graus < 0:
            graus = 360 + graus
        self.ang = graus
   
    def toRad(self):
        return Radianos(self.ang * pi / 180)

class Radianos:
    def __init__(self, rad):
        self.ang = rad
    
    def toGraus(self):
        return Graus(self.ang * 180 / pi)

class Polar:
    def __init__(self, r, theta):
        self.r = r
        if type(theta) == Graus:
            self.theta = theta.toRad()
        else:
            self.theta = theta

    def __complex__(self):
        return complex(self.r * cos(self.theta.ang), self.r * sin(self.theta.ang))

class Complexo():
    def __init__(self, num):
        self.origin = "Rec" if type(num) == complex else "Pol"
        if type(num) != complex:
            num = complex(num)
        self.num = num
    
    def print(self, RadDeg):
        if self.origin == "Pol":
            angle = Radianos(atan2(self.num.imag, self.num.real))
            return f"{round(abs(self.num), 2)} ∠ {round(angle.ang, 2) if RadDeg == 'R' else round(angle.toGraus().ang)}{'°' if RadDeg == 'G' else 'rad'}"
        else:
            return f"{round(self.num.real, 2)} + {round(self.num.imag, 2)}j"
    def sympy(self):
        if self.origin == "Pol":
            angle = Radianos(atan2(self.num.imag, self.num.real))
            return f"{round(abs(self.num), 2)}*exp({round(angle.ang, 2)}*I)"
        else:
            return f"{round(self.num.real, 2)} + {round(self.num.imag, 2)}*I"
    def __add__(self, other):
        self.num += other.num
        return self

    def __sub__(self, other):
        self.num -= other.num
        return self

    def __mul__(self, other):
        self.num *= other.num
        return self
    
    def __truediv__(self, other): 
        if other.num == 0:
            raise ZeroDivisionError("Divisão por zero")
        self.num /= other.num
        return self

    def __complex__(self):  
        return self.num