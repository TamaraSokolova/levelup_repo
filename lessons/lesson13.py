class Animal():
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def display_info(self):
        print(f'{self.name} - {self.species}')

class Mammal(Animal):
        def __init__(self, name, species, warm_blood):
            super().__init__(name, species)
            self.warm_blood = True

        def display_info(self):
            print(f'warm_blood {self.name} - {self.species}, {self.warm_blood}')

class Bird(Animal):
        def __init__(self, name, species, warm_blood):
            super().__init__(name, species)
            self.can_fly = True

        def display_info(self):
            print(f'can_fly {self.name} - {self.species}, {self.can_fly}')

zebra = Animal(zebra, mammal)
    
'''class Zoo():
    def __init__(self, animals):
        self.animals = animals

    def add_animal(self, animals):
        print(animals)
    
    def show_all_animals(self):
        print ('животные')
        for i in animals:
            self.i.append(animals)'''

