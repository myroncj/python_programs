'''
Create a class called rainbow with 7 colours.
One method to display rainbow.

'''

class rainbow:
    def __init__(self): # The __init()__ function is used as a constructor
        self.c1 = 'violet'
        self.c2 = 'indigo'
        self.c3 = 'blue'
        self.c4 = 'green'
        self.c5 = 'yellow'
        self.c6 = 'orange'
        self.c7 = 'red'
        
    def display_rainbow(self):
        print(self.c1)
        print(self.c2)
        print(self.c3)
        print(self.c4)
        print(self.c5)
        print(self.c6)
        print(self.c7)

rb1=rainbow()

rb1.display_rainbow()