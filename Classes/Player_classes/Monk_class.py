from OOP_DnD_like_game.Classes.Player_class import *


class Monk(Player):
    def __init__(self, level, name):
        class_info = "Монах "
        super().__init__(
            level=level,
            name=f"Монах {name}",
            magical_level=level,
            max_hp=50 * level,
            atk=40 * level,
            defense=6 * level,
            money=18)
