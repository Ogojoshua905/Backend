class Pets():
    cat = "Dog"
    def __init__(self, name, age, species, color, voice):
        self.name = name
        self.age = age
        self.voice = voice
        self.species = species
        self.color = color
    def action(self):
        return f"{self.name} is My {self.cat} he's just {self.age}, he's a {self.species} he has a {self.color}ish color fur, and he loves {self.voice}ing at Strangers he don't know"
    
petsact = Pets("Benimaru", "18 Months", "German_Shepherd", "Grey", "Bark")
print(petsact.action())