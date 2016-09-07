

# Creating classes to demo inheritance

class Animal:
    def eat(self):
        print('animal crunch')
    def talk(self):
        print('making some animal noise')

class Cat(Animal):
    def talk(self):
        print('cats meow')

    def invisibility(self):
        print('cats can vanish...')

# define fluffy as an animal of the cat variety
fluffy = Cat()

fluffy.talk()
fluffy.eat()
fluffy.invisibility()
