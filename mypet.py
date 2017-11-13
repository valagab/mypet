from pet import Pet

class Mypet(Pet):
    def __init__(self, name, age, tipology, owner):
        Pet.__init__(self, name, age, tipology)
        self.owner = owner
    
    def say_hello(self):
        if self.tipology == 'cat':
            print('meow')
        elif self.tipology == 'dog':
            print('bau')
        elif self.tipology == 'horse':
            print('hihihi')




f = Mypet('Arazio', 15, 'dog', 'Gabriele')
f.hello()
print(f.owner)
f.say_hello()

g = Mypet('Iaffiu', 4, 'cat', 'Marco')
g.hello()
print(g.owner)
g.say_hello()

i = Mypet('Sariddu', 2, 'horse', 'Nancy')
i.hello()
print(i.owner)
i.say_hello()