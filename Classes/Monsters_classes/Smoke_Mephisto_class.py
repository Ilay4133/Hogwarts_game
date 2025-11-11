from Classes.Monster_class import *


class Smoke_Mephisto(Monster):
    def __init__(self, level):
        monster_info = "Дымный мефит"
        super().__init__(
            name=f"Дымный мефит ({level})",
            level=level,
            magical_level=level,
            max_hp=100 * level,
            atk=24 * level,
            defense=18 * level,
            loot={"монеты": [23, 0.7],
                  "мефитовый дым": {"количество": 30, "шанс выпадения": 0.8, "стоимость": 1, "описание": "___"},
                  "дух мефита": {"количество": 1, "шанс выпадения": 0.2, "стоимость": 1, "описание": "___"}})
