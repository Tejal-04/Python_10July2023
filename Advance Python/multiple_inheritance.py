'''class Father():
    def gardening(self):
        print("I enjoy Gardening")

class Mother():
    def cooking(self):
        print("I Love Cooking")

class Child(Mother,Father):
    def sports(self):
        print("I enjoy sports")        
        
c = Child()
c.cooking()
c.gardening()
c.sports()        '''

class Father():
    def skills(self):
        print("Gardening, Programming")

class Mother():
    def skills(self):
        print("Cooking, Art")

class Child():
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Sports") 

c = Child()
c.skills()                     