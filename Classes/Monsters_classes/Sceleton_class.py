from Classes.Monster_class import *


class Sceleton(Monster):
    def __init__(self, level):
        monster_info = "Скелет"
        super().__init__(
            level=level,
            name=f"Скелет ({level})",
            magical_level=level,
            max_hp=60 * level,
            atk=16 * level,
            defense=5 * level,
            loot={"монеты": [10, 0.7],
                  "кости": {"количество": 40, "шанс выпадения": 1, "стоимость": 1, "описание": "___"},
                  "череп скелета": {"количество": 1, "шанс выпадения": 0.3, "стоимость": 1, "описание": "___"}},
            looting_exp = 100)
