from Classes.Player_class import *


class Wizard(Player):
    def __init__(self, level, name):
        class_info = "Волшебник"
        super().__init__(
            level=level,
            name=f"Волшебник {name}",
            magical_level=level,
            max_hp=60 * level,
            atk=17 * level,
            defense=5 * level,
            money=24)
