import random

class Pokemon():
    def __init__(self,name,level,hp, max_hp,atk,defens,typex):
        self.name = name
        self.level = level
        self.hp = hp
        self.max_hp = max_hp
        self.atk = atk
        self.defens = defens
        self.typex = typex
        self.tamed = False

    def damaged(self, damage):
        self.hp = self.hp - damage
        return self.hp

    def attack(self):
        pass


    def healing(self):
        self.hp = self.max_hp
        return self.hp

    def speak(self):
        pass


class Trainer():
    def __init__(self, name):
        self.name = name
        self.pokemons = []
        self.active_pokemon = None

    def catch_pokemon(self, pokemon):
        pass

    def attack_oponent(self):
        print("Выберите покемона:", self.pokemons)
        pokemon_chaise_index = int(input("Введите номер в списке: "))
        choised_pokemon = self.pokemons[pokemon_chaise_index]

    def health_pokemons(self):
        for pokemon in self.pokemons:
            pokemon.healing

class Pikachu(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Pikachu", level,
                         hp=10*level,
                         max_hp = 10*level,
                         atk=3*level,
                         defens = 2*level,
                         typex = "Electric")

    def speak(self):
        print("Pika-Pika!")

def wild_battle(trainer, wild_trainer):

    print("Попытатся атаковать (D) или попытатся поймать (F)")
    deist = str(input("Выберите действие: "))
    if deist == 'F' or 'f':
        catch_chanse = (1 - wild_pokemon.level/pokemon.level)*0,5



def main():
    player = Trainer("Тест")
    starter = random.choise([Pikachu(),])
    player.catch_pokemon(starter)
