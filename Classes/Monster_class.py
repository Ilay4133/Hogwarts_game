import random
import threading


class Monster:
    def __init__(self, loot, level, name, magical_level, max_hp, atk, defense, looting_exp):
        self.level = level
        self.name = name
        self.magical_level = magical_level
        self.max_hp = max_hp
        self.hp = max_hp
        self.atk = atk
        self.defens = defense
        self.loot = loot
        self.h_timer: bool = True
        self.looting_exp = looting_exp

    def attack(self, opponent, defense_bool, coef) -> list:
        print("Враг атакует")
        if defense_bool != 0:
            return [round(opponent.hp, 2), "Игрок парировал атаку", 1]
        else:
            damage = self.atk * coef
            opponent.hp = opponent.hp - damage
            return [round(opponent.hp, 2), damage, 0]

    def healing(self) -> list or None:
        healing_time = 25

        def timer():
            self.h_timer = True

        if self.h_timer:
            healing_hp = self.hp + 30
            if healing_hp > self.max_hp:
                self.hp = self.max_hp
                self.h_timer = False
            else:
                self.hp = self.hp + 30
                self.h_timer = False
            thread = threading.Timer(15, timer)
            thread.start()
            return [round(self.hp, 2), healing_time]
        else:
            return None

    @staticmethod
    def defensing() -> int:
        return 1

    def player_looting(self, player) -> list:
        got_loot = {}
        monster_loot = self.loot
        money_count = 0
        for i in monster_loot:
            item = i
            probability = float(random.random())
            if item == "монеты":
                chance = monster_loot[item][1]
                if probability <= chance:
                    loot_count_coef = random.randint(1, 100)
                    loot_count = int((monster_loot[item][0] * (loot_count_coef / 100)) // 1)
                    player.money = player.money + loot_count
                    money_count = loot_count
                else:
                    pass
            else:
                chance = monster_loot[item]["шанс выпадения"]
                if monster_loot[item]["количество"] != 1:
                    if probability <= chance:
                        loot_count_coef = random.randint(1, 100)
                        loot_count = int((monster_loot[item]["количество"] * (loot_count_coef / 100)) // 1)
                        if loot_count != 0:
                            got_loot.update({item: loot_count})
                        else:
                            pass
                    else:
                        pass

                else:
                    if probability <= chance:
                        loot_count = 1
                        got_loot.update({item: loot_count})
                    else:
                        pass
        for j in got_loot:
            looting_item = j
            looting_item_dic = {"количество": got_loot[looting_item]} | dict(list(self.loot[j].items())[2:4])
            player.inventory.update({looting_item: looting_item_dic})
        if player.exp >= player.level_up_exp:
            player.level_up
            level_up = 1
        else:
            level_up = 0
        return [got_loot, player.inventory, money_count, level_up]

    def level_up(self) -> None:
        self.level += 1
        return None
