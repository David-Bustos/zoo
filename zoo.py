class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animals(self, name):
        self.animals.append( name)

    # def add_koala(self, name, age, health, happiness):
    #     self.animals.append( Koala(name, age, health, happiness) )

    # def add_lion(self, name, age, health, happiness):
    #     self.animals.append( Lion(name, age, health, happiness) )

    # def add_tiger(self, name, age, health, happiness):
    #     self.animals.append( Tiger(name, age, health, happiness) )

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

class Animal:
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def feeding(self):
        self.health += 10
        self.happiness += 10
        return self

    def display_info(self):
        print(f"Estado de {self.name} ({self.__class__.__name__})\nSalud: {self.health}\nFelicidad: {self.happiness}")
        return self

class Wolf(Animal):
    def __init__(self, name, age, health, happiness):
        super().__init__(name, age, health, happiness)
        self.sound = {'aullido': 'AUUU'}

class Koala(Animal):
    def __init__(self, name, age, health, happiness):
        super().__init__(name, age, health, happiness)

class Tiger(Animal):
    def __init__(self, name, age, health, happiness):
        super().__init__(name, age, health, happiness)
        self.sound = {'Rugido': 'GRRR'}

class Lion(Animal):
    def __init__(self, name, age, health, happiness):
        super().__init__(name, age, health, happiness)
        self.sound = {'Rugido': 'GRRR'}

myzoo = Zoo("David's Zoo")
balto = Wolf('Balto', 8, 100, 70)
myzoo.add_animals(balto)
alex = Lion('Alex', 8, 80, 50)
myzoo.add_animals(alex)

balto.feeding().feeding().display_info()

myzoo.print_all_info()
