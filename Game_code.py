import random
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
        self.defens = defense
        self.inventory = {}
        self.money = money
        self.h_timer: bool = True

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

    def open_inventory(self):
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
                  f"ХП сейчас: {self.hp}")




class Warrior(Player):
    def __init__(self, level, name):
        class_info = "Воин"
        super().__init__(
            level=level,
            name=f"Воин {name}",
            magical_level=level,
            max_hp=70 * level,
            atk=25 * level,
            defense=10 * level,
            money=35)


class Wizard(Player):
    def __init__(self, level, name):
        class_info = "Волшебник"
        super().__init__(
            level=level,
            name=f"Волшебник {name}",
            magical_level=level,
            max_hp=60 * level,
            atk=17 * level,
            defense=5 * level,
            money=24)


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


class Paladin(Player):
    def __init__(self, level, name):
        class_info = "Паладин"
        super().__init__(
            level=level,
            name=f"Паладин {name}",
            magical_level=level,
            max_hp=80 * level,
            atk=30 * level,
            defense=18 * level,
            money=40)


class Shop:
    def __init__(self):
        self.showcase = {"зелье": {"стоимость": 20, "описание": "Восстанавливает 30 HP", 'type':  ['heal', 30]},
                         "хлеб": {"стоимость": 2, "описание": "Восстанавливает 3 HP", 'type': ['heal', 3]},
                         "гримуар": {"стоимость": 50, "описание": "Добавляет 20 урона на ход", 'type':  ['dmg_up', 20]},
                         "мифическое яблоко": {"стоимость": 999, "описание": "Увеличивает уровень игрока на 20 единиц",
                                               'type':  ['lvl_up', 3]}}

    def show_showcase(self) -> None:
        print("\nВитрина: ")
        for key, value in self.showcase.items():
            print(f"| {key.upper()} |")
            for v_key, v_value in value.items():
                if v_key != "type":
                    print(f"| {v_key} - {v_value}")
                else:
                    pass
            print("|_________________________________________|")
        return None

    def sell(self, player, purchases) -> None or list:
        expenses = 0
        new_items = {}
        player_money = player.money
        for product in purchases:
            if product in self.showcase:
                price = int(self.showcase[str(product)]["стоимость"]) * purchases[product]
                count = purchases[product]
                expenses = expenses + price
                new_items.update({product: count})
            else:
                print("Shop.NO_PURCHASE_DATA")
        if expenses > player_money:
            print("У вас не хватает монет")
            return None
        else:

            for item in new_items:
                if item in player.inventory:
                    all_count = new_items[item] + player.inventory[item]["количество"]
                    buying_item_dict = {"количество": all_count} | self.showcase[item]
                else:
                    count = new_items[item]
                    buying_item_dict = {"количество": count} | self.showcase[item]
                if buying_item_dict["стоимость"] != 1:
                    buying_item_dict["стоимость"] = self.showcase[item]["стоимость"] // 2
                else:
                    pass
                player.inventory.update({item: buying_item_dict})
            player.money = player_money - expenses
            return [player.money, player.inventory]

    def buy(self, player, sales_dict) -> None or list:
        player_earnings_money = 0
        for item in sales_dict:
            if sales_dict[item] > player.inventory[item]["количество"]:
                print("У вас нет столько предметов")
                return None
            else:
                pass

        for item in sales_dict:
            if item in player.inventory:
                count = sales_dict[item]
                if count > 0:
                    player_earnings_money += player.inventory[item]["стоимость"] * count
                    if count == player.inventory[item]["количество"]:
                        if item in self.showcase:
                            pass  # Потом сделать систему ограниченных покупок и продаж
                        else:
                            self.showcase.update({item: player.inventory[item]})
                            self.showcase[item]["количество"] = count
                        del player.inventory[item]
                    else:
                        player.inventory[item]["количество"] -= count
                        if item in self.showcase:
                            pass  # Потом сделать систему ограниченных покупок и продаж
                        else:
                            self.showcase.update({item: player.inventory[item]})
                            self.showcase[item]["количество"] = count
                else:
                    pass
            else:
                print(f"Такого предмета ({item}) нет в  вашем инвентаре")

        player.money += player_earnings_money
        print("\n")
        return [player.money, player.inventory]


class Monster:
    def __init__(self, loot, level, name, magical_level, max_hp, atk, defense):
        self.level = level
        self.name = name
        self.magical_level = magical_level
        self.max_hp = max_hp
        self.hp = max_hp
        self.atk = atk
        self.defens = defense
        self.loot = loot
        self.h_timer: bool = True

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
        return [got_loot, player.inventory, money_count]

    def level_up(self) -> None:
        self.level += 1
        return None


class Sceleton(Monster):
    def __init__(self, level):
        super().__init__(
            monster_info = "Скелет",
            level=level,
            name=f"Скелет ({level})",
            magical_level=level,
            max_hp=60 * level,
            atk=16 * level,
            defense=5 * level,
            loot={"монеты": [10, 0.7],
                  "кости": {"количество": 40, "шанс выпадения": 1, "стоимость": 1, "описание": "___"},
                  "череп скелета": {"количество": 1, "шанс выпадения": 0.3, "стоимость": 1, "описание": "___"}})


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
                  "шапка культиста": {"количество": 1, "шанс выпадения": 0.3, "стоимость": 1, "описание": "___"}})


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
                  "волосы Дроу": {"количество": 1, "шанс выпадения": 0.1, "стоимость": 1, "описание": "___"}})


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
                  "череп бабау": {"количество": 4, "шанс выпадения": 0.2, "стоимость": 1, "описание": "___"}})


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


sceleton = Sceleton(1)
cultist = Cultist(1)
babau = Babau(1)
bone_naga_spirit = Bone_Naga_Spirit(1)
drow = Drow(1)
smoke_mephisto = Smoke_Mephisto(1)
dragon = Dragon(1)
# __________
shop = Shop()

all_monsters_list = [sceleton, cultist, babau, bone_naga_spirit, dragon,drow, smoke_mephisto]


# cultist, babau, bone_naga_spirit, dragon,drow, smoke_mephisto


def kubik(kubiks_edges=25) -> float:
    kubik_val = random.randint(1, kubiks_edges)
    kubik_koef = round((kubik_val / kubiks_edges), 1)
    return kubik_koef


def new_player_create() -> object:
    player_name = str(input("Создание игрока, введите имя: "))
    choose_class = int(input("Выберите класс: \n- Воин (1)\n- Волшебник (2)\n- Монах (3)"
                             "\n- Паладин (4)\n> "))
    if choose_class == 1:
        Player = Warrior(1, player_name)
    elif choose_class == 2:
        Player = Wizard(1, player_name)
    elif choose_class == 3:
        Player = Monk(1, player_name)
    elif choose_class == 4:
        Player = Paladin(1, player_name)
    else:
        Player = Warrior(1, player_name)
    return Player


def battle(player) -> None:
    player_defensing = 0
    opponent_defensing = 0
    opponent = all_monsters_list[random.randint(0, (len(all_monsters_list)) - 1)]
    print(f"Ваш оппонент: {opponent.name}")
    time.sleep(1)

    while True:

        opponent_defensing = 0
        opponent_action = random.randint(0, 2)

        if opponent_action == 0:
            opponent_coef = kubik()
            print(f"Кубик: {opponent_coef}")
            attack_inf = opponent.attack(player, player_defensing, opponent_coef)
            if attack_inf[2] == 1:

                print(attack_inf[1])
            else:
                print(f"Враг нанес вам {attack_inf[1]} урона, у вас осталось {attack_inf[0]} HP")

        elif opponent_action == 1:
            opponent_defensing = opponent.defensing()
            print(f"Враг защитился")

        elif opponent_action == 2:
            healing_data = opponent.healing()
            if healing_data is not None:
                print(f"Враг вылечился, HP сейчас: {healing_data[0]},"
                      f" (задержка восстановления ХП: {healing_data[1]} сек.)\n")
            else:
                print("Задержка восстановления ХП")

        print("_____________________")

        if player.hp <= 0:
            print(f"{opponent.name}, победил!")
            print("_____________________")
            break

        elif opponent.hp <= 0:
            print(f"{player.name}, победил!")
            looting_data = opponent.player_looting(player)
            print(
                f"{player.name} получил: {looting_data[0]}.\n Инвентарь сейчас: {looting_data[1]}, "
                f"монеты: {player.money} (+{looting_data[2]}) \n_____________________")
            break

        player_defensing = 0
        print("\nВыберите действие:")
        action = str(input("Атаковать - A\n"
                           "Парировать - D\n"
                           "Лечится - H\n"
                           "Открыть инвентарь - I\n"
                           "> "))
        print("")
        up_action = action.upper()

        if up_action == "A":
            player_coef = kubik()
            print(f"Кубик: {player_coef}")
            attack_inf = player.attack(opponent, opponent_defensing, player_coef)
            print(f"Вы нанесли врагу {attack_inf[1]} урона, у врага осталось {attack_inf[0]} HP")

        elif up_action == "D":
            player_defensing = player.defensing()
            print(f"Вы парировали атаку")

        elif up_action == "H":
            healing_data = player.healing()
            if healing_data is not None:
                print(f"Вы вылечились, HP сейчас: {healing_data[0]},"
                      f" (задержка восстановления ХП: {healing_data[1]} сек.)\n")
            else:
                print("Задержка восстановления ХП")
        elif up_action == "I":
            inbentory_data = player.open_inventory()
        else:
            pass

        if player.hp < 0:
            print(f"{opponent.name}, победил! \n")
            break

        elif opponent.hp < 0:
            print(f"{player.name}, победил!")
            looting_data = opponent.player_looting(player)
            print(
                f"{player.name} получил: {looting_data[0]}.\n Инвентарь сейчас: {looting_data[1]}, "
                f"монеты: {player.money} + ({looting_data[2]}) \n_____________________")
            break

    return None


def shopping(player, shop) -> None:
    while True:
        shop_select = str(input("\n_____________________"
                                "\nПриветствуем в магазине.\n"
                                "B - Купить\n"
                                "S - продать\n"
                                "Q - Вернуться\n"
                                "> "))
        up_shop_select = shop_select.upper()
        if up_shop_select == "B":
            purchases_dict = {}
            print(f"\nЧто бы вы хотели приобрести?")
            print(f"Монеты: {player.money}")
            shop.show_showcase()
            while True:
                try:
                    purchases_select, count = map(str, input(
                        f"\nВведите название или выйдете - Q Q (покупка завершится) \n> ").split())
                except ValueError:
                    print("Не введено: товар или количество товара либо только одно Q")
                else:
                    if purchases_select != "Q":
                        if purchases_select in purchases_dict:
                            purchases_dict[purchases_select] = purchases_dict[purchases_select] + int(count)
                        else:
                            purchases_dict.update({purchases_select: int(count)})
                    else:
                        if purchases_dict != {}:
                            sell_data = shop.sell(player, purchases_dict)
                            if sell_data is not None:
                                print("\n|________________________________________|")
                                print(f"Монеты игрока: {sell_data[0]}, инвентарь:")
                                print("|________________________________________|")
                                for key, value in sell_data[1].items():
                                    print(f"| {key.upper()} |")
                                    for v_key, v_value in value.items():
                                        if v_key != "type":
                                            print(f"| {v_key} - {v_value}")
                                        else:
                                            pass
                                    print("|________________________________________|")

                            else:
                                pass
                        else:
                            pass
                        break
        elif up_shop_select == "S":
            sells_dict = {}
            print(f"\nЧто бы вы хотели продать?\n")
            player.see_inventory()
            while True:
                try:
                    buy_select, count = map(str, input(
                        f"\nВведите название или выйдете - Q Q (продажа завершится) \n> ").split())
                except ValueError:
                    print("Не введено: товар или количество товара либо только одно Q")
                else:
                    if buy_select != "Q":
                        if buy_select in sells_dict:
                            sells_dict[buy_select] = sells_dict[buy_select] + int(count)
                        else:
                            sells_dict.update({buy_select: int(count)})
                    else:
                        if sells_dict != {}:
                            buy_data = shop.buy(player, sells_dict)
                            if buy_data is not None:
                                print("|________________________________________|")
                                print(f"\nМонеты игрока: {buy_data[0]}, инвентарь:\n")
                                print("|________________________________________|")
                                for key, value in buy_data[1].items():
                                    print(f"| {key.upper()} |")
                                    for v_key, v_value in value.items():
                                        if v_key != "type":
                                            print(f"| {v_key} - {v_value}")
                                        else:
                                            pass
                                    print("|________________________________________|")
                                shop.show_showcase()

                            else:
                                pass
                        else:
                            pass
                        break

        elif up_shop_select == "Q":
            break
        else:
            pass
    return None


def main(start) -> int:
    global main_Player
    if start == 1:
        print("Приветствуем вас в мире меча и магии!")
        main_Player = new_player_create()
        start = 0
    while True:
        main_select = str(input("\nЧто хотите сделать? \n"
                                "A - Cразиться\n"
                                "S - Магазин\n"
                                "C - Пойти к костру\n"
                                "I - Инвентарь\n"
                                "Q - Выход\n"
                                "> "))
        up_main_select = main_select.upper()
        if up_main_select == "A":
            if main_Player.hp <= 0:
                print("Ваше здоровье низкое, вы не можете вступить в бой.")
            else:
                battle(main_Player)
        elif up_main_select == "S":
            shopping(main_Player, shop)
        elif up_main_select == "C":
            if main_Player.hp <= 0:
                main_Player.campfiring()
            else:
                print("Ваше здоровье в порядке")

        elif up_main_select == "I":
            main_Player.see_inventory()
        elif up_main_select == "Q":
            break
        else:
            pass

    return 0


if __name__ == '__main__':
    start = 1
    main(start)
