from Classes.Monster_class import *


class Babau(Monster):
    def __init__(self, level):
        monster_info = "Бабау"
        super().__init__(
            name=f"Бабау ({level})",
            level=level,
            magical_level=level,
            max_hp=70 * level,
            atk=20 * level,
            defense=10 * level,
            loot={"монеты": [5, 0.7],
                  "шкура": {"количество": 9, "шанс выпадения": 1, "стоимость": 1, "описание": "___"},
                  "череп бабау": {"количество": 4, "шанс выпадения": 0.2, "стоимость": 1, "описание": "___"}},
            looting_exp = 180)
