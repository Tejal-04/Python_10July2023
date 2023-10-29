class Vehicle:
    def general_usage(self):
        print('General Use : Transporation')

class Car(Vehicle):
    def __init__(self):
        print("I'm Car")
        self.wheels = 4
        self.has_roof = True
    def specific_usage(self):
        print("Specific Usage : Commute to work, Vacation with Family")

class MotorCycle(Vehicle):
    def __init__(self):
        print("I'm MotorCycle")
        self.wheels = 2
        self.has_roof = False
    def specific_usage(self):
        print("Specific Usage : Road Trip, Racing")

c = Car()
c.general_usage()
c.specific_usage()
print(c.has_roof)
print(c.wheels)
# checks the object is instance of class or not
print(isinstance(c,Car))


m = MotorCycle()
m.general_usage()
m.specific_usage()
print(m.wheels)
print(m.has_roof)
print(isinstance(m,MotorCycle))
print(isinstance(m,Car))

print(issubclass(Car,Vehicle))
print(issubclass(Car,MotorCycle))