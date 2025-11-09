from OOP_DnD_like_game.Classes.Monster_class import *


class Dragon(Monster):
    def __init__(self, level):
        monster_info = "Дракон"
        super().__init__(
            level=level,
            name=f"Дракон ({level})",
            magical_level=level,
            max_hp=350 * level,
            atk=61 * level,
            defense=32 * level,
            loot={"монеты": [70, 0.7],
                  "чешуя дракона": {"количество": 60, "шанс выпадения": 0.4, "стоимость": 1, "описание": "___"},
                  "коготь дракона": {"количество": 4, "шанс выпадения": 0.2, "стоимость": 1, "описание": "___"}})
