from OOP_DnD_like_game.Classes.Monster_class import *


class Bone_Naga_Spirit(Monster):
    def __init__(self, level):
        monster_info = "Костяной Нага Дух"
        super().__init__(
            name=f"Костяной Нага Дух ({level})",
            level=level,
            magical_level=level,
            max_hp=70 * level,
            atk=20 * level,
            defense=10 * level,
            loot={"монеты": [15, 0.7],
                  "кости": {"количество": 70, "шанс выпадения": 1, "стоимость": 1, "описание": "___"},
                  "череп Нага Духа": {"количество": 1, "шанс выпадения": 0.15, "стоимость": 1, "описание": "___"}})
