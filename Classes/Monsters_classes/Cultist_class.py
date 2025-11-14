from Classes.Monster_class import *


class Cultist(Monster):
    def __init__(self, level):
        monster_info = "Культист"
        super().__init__(
            level=level,
            name=f"Культист ({level})",
            magical_level=level,
            max_hp=78 * level,
            atk=30 * level,
            defense=0 * level,
            loot={"монеты": [12, 0.7],
                  "обрывки одежды культиста": {"количество": 13, "шанс выпадения": 1, "стоимость": 1,
                                               "описание": "___"},
                  "шапка культиста": {"количество": 1, "шанс выпадения": 0.3, "стоимость": 1, "описание": "___"}},
            looting_exp = 130)
