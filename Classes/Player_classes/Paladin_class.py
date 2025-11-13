from Classes.Player_class import *


class Paladin(Player):
    def __init__(self, level, name):
        class_info = "Паладин"
        super().__init__(
            level=level,
            name=f"Паладин {name}",
            magical_level=level,
            max_hp=80 * level,
            atk=30 * level,
            defense=18 * level,
            money=40)
