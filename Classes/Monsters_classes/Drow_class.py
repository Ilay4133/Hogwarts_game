from Classes.Monster_class import *


class Drow(Monster):
    def __init__(self, level):
        monster_info = "Дроу"
        super().__init__(
            name=f"Дроу ({level})",
            level=level,
            magical_level=level,
            max_hp=85 * level,
            atk=18 * level,
            defense=30 * level,
            loot={"монеты": [17, 0.7],
                  "обрывки одежды": {"количество": 10, "шанс выпадения": 1, "стоимость": 1, "описание": "___"},
                  "волосы Дроу": {"количество": 1, "шанс выпадения": 0.1, "стоимость": 1, "описание": "___"}},
            looting_exp = 200)
