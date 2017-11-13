import random

class Pet:
    def __init__(self, name, age, tipology):
        self.name = name
        self.age = age
        self.tipology = tipology

    def hello(self):
        print('The name of my animal is ' + self.name, 'it is a ' + self.tipology, 'and is ' + str(self.age), 'years old')

    def eat(self):
        if self.tipology == 'dog':
            print(0)
        elif self.tipology == 'cat':
            print(0)
        else:
            print(1)

    def jump(self):
        for i in range(1):
            numcasuale = random.randint(0,10)
            print(numcasuale)

a = Pet('Pippo', 10, 'cat')
a.hello()
a.eat()
a.jump()

b = Pet('Pluto', 5, 'dog')
b.hello()
b.eat()
b.jump()

c = Pet('Varenne', 12, 'horse')
c.hello()
c.eat()
c.jump()

d = Pet('Nemo', 1, 'fish')
d.hello()
d.eat()
d.jump()

e = Pet('Turi', 1, 'cat')
e.hello()
e.eat()
e.jump()
