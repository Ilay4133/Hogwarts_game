import threading
import time
from tqdm import tqdm


class Player:
    def __init__(self, level, name, magical_level, max_hp, atk, defense, money):
        self.level = level
        self.name = name
        self.magical_level = magical_level
        self.max_hp = max_hp
        self.hp = max_hp
        self.atk = atk
        self.min_atk = atk
        self.defens = defense
        self.inventory = {}
        self.money = money
        self.h_timer: bool = True
        self.exp = 0
        self.level_up_exp = 1000+1000*(level/1000)

    def attack(self, opponent, defense_bool, coef) -> list:
        if defense_bool != 0:
            damage = self.atk * coef - opponent.defens
            if damage < 0:
                opponent.hp = opponent.hp + damage
                return [round(opponent.hp, 2), -damage]
            else:
                opponent.hp = opponent.hp - damage
                return [round(opponent.hp, 2), damage]
        else:
            damage = self.atk * coef
            opponent.hp = opponent.hp - damage
            return [round(opponent.hp, 2), damage]

    def healing(self) -> list or None:
        healing_time = 15

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
            thread = threading.Timer(healing_time, timer)
            thread.start()
            return [round(self.hp, 2), healing_time]
        else:
            return None

    @staticmethod
    def defensing() -> int:
        return 1

    def see_inventory(self) -> None:
        print("\n|________________________________________|")
        print(f"Монеты: {self.money}")
        print("|________________________________________|")
        for key, value in self.inventory.items():
            print(f"| {key.upper()} |")
            for v_key, v_value in value.items():
                if v_key != "type":
                    print(f"| {v_key} - {v_value}")
                else:
                    pass
            print("|________________________________________|\n")
        return None

    def campfiring(self, campfire_time=10) -> None:
        print(f"Вы у костра, подождите {campfire_time} секунд чтобы восстановить здоровье")
        for i in tqdm(range(100)):
            time.sleep(campfire_time / 100)
        print("Вы посидели у костра, ваше здоровье восстановилось")
        self.hp = self.max_hp
        return None

    def open_inventory(self) -> str:
        print("\n|________________________________________|")
        print(f"Монеты: {self.money}")
        print("|________________________________________|")
        for key, value in self.inventory.items():
            print(f"| {key.upper()} |")
            for v_key, v_value in value.items():
                if v_key != "type":
                    print(f"| {v_key} - {v_value}")
                else:
                    pass
            print("|________________________________________|")
        invent_chose = str(input("Что использовать или выйти - Q\n> "))
        chose_data = self.inventory[invent_chose]
        if chose_data["type"][0] == "heal":
            print("heal")
            healing_hp = chose_data["type"][1]
            if self.hp + healing_hp > self.max_hp:
                self.hp = self.max_hp
            else:
                self.hp += healing_hp
            print(f"Вы восстановили {healing_hp} ХП, \n"
                  f"ХП сейчас: {self.hp}\n_____________________")

        elif chose_data["type"][0] == "dmg_up":
            print("dmg_up")
            atk_up = chose_data["type"][1]
            self.atk += atk_up
            print(f"Вы увеличили атаку на {atk_up} ед на один ход, \n"
                  f"Атака сейчас: {self.hp} (дальше последует атака)\n_____________________")

        elif chose_data["type"][0] == "lvl_up":
            print("dmg_up")
            level_up = chose_data["type"][1]
            self.level += level_up
            print(f"Вы увеличили уровень на {level_up} ед, \n"
                  f"Уровень  сейчас: {self.hp}\n_____________________")

        return chose_data["type"][0]

    def level_up(self) -> None:
        self.level += 1
        return None
