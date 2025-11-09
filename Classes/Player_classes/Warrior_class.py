from OOP_DnD_like_game.Classes.Player_class import *


class Warrior(Player):
    def __init__(self, level, name):
        class_info = "Воин"
        super().__init__(
            level=level,
            name=f"Воин {name}",
            magical_level=level,
            max_hp=70 * level,
            atk=25 * level,
            defense=10 * level,
            money=35)
