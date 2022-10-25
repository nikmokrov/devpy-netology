class Farm_animal():
    def __init__(self, name, weight=0, animal_type='Farm animal', voice='', product=''):
        self.name = name
        self.weight = weight
        self.animal_type = animal_type
        self.voice = voice
        self.product = product

    def call(self):
        print(f"{self.animal_type} {self.name} says {self.voice}!")
    def feed(self, food):
        print(f"{self.animal_type} {self.name} eats {food}")
    def pick(self):
        if self.product != '':
            print(f"{self.animal_type} {self.name} give some {self.product}")
        else:
            print(f"{self.animal_type} {self.name} give nothing")

class Goose(Farm_animal):
    def __init__(self, name, weight):
        super().__init__(name, weight, animal_type="goose", voice="Ga-Ga", product="eggs")

class Cow(Farm_animal):
    def __init__(self, name, weight):
        super().__init__(name, weight, animal_type="cow", voice="Moo", product="milk")

class Sheep(Farm_animal):
    def __init__(self, name, weight):
        super().__init__(name, weight, animal_type="sheep", voice="Bee", product="wool")

class Chiken(Farm_animal):
    def __init__(self, name, weight):
        super().__init__(name, weight, animal_type="chiken", voice="Ko-ko-ko", product="eggs")

class Goat(Farm_animal):
    def __init__(self, name, weight):
        super().__init__(name, weight, animal_type="goat", voice="Mee", product="milk")

class Duck(Farm_animal):
    def __init__(self, name, weight):
        super().__init__(name, weight, animal_type = "duck", voice = "Quak")

farm = {'seriy': Goose("Seriy", 7),
        'beliy': Goose("Beliy", 8),
        'manka': Cow("Manka", 25.2),
        'barashek': Sheep("Barashek", 12.8),
        'kudryaviy': Sheep("Kudryaviy", 13.5),
        'roga': Goat("Roga", 8),
        'kopyta': Goat("Kopyta", 9),
        'kryakva': Duck("Kryakva", 5.2)}

for animal in farm.values():
    animal.call()
    animal.feed('grass')
    animal.pick()

sum_weight = sum(animal.weight for animal in farm.values())
max_weight_name = sorted(farm.values(), key=lambda x: x.weight, reverse=True)[0].name
max_weight = sorted(farm.values(), key=lambda x: x.weight, reverse=True)[0].weight
print(f"Total weigth: {sum_weight}")
print(f"Max weigth: {max_weight_name}, {max_weight}")
