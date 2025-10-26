import random
import time

class Player():
    def __init__(self, level, name, magical_level, max_hp, atk, defens, money):
        self.level = level
        self.name = name
        self.magical_level = magical_level
        self.max_hp = max_hp
        self.hp = max_hp
        self.atk = atk
        self.defens = defens
        self.inventory = {}
        self.money = money

    def attack(self, oponent, defens_bool, coef):
        if defens_bool != 0:
            damage = self.atk*coef-oponent.defens
            if damage < 0:
                oponent.hp = oponent.hp + damage
                return [round(oponent.hp, 2), -(damage)]
            else:
                oponent.hp = oponent.hp - damage
                return [round(oponent.hp, 2), damage]
        else:
            damage = self.atk*coef
            oponent.hp = oponent.hp - damage
            return [round(oponent.hp, 2), damage]

    def healing(self):
        healing_hp = self.hp + 30
        if healing_hp > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp = self.hp + 30
        return round(self.hp, 2)

    def defensing(self):
        return 1

    def see_inventory(self):
        for item in self.inventory:
            print(f"{item}: {self.inventory[item]}")
        print(f"Монеты: {self.money}")

class Warrior(Player):
    def __init__(self, level, name):
        class_info = "Воин"
        super().__init__(
            level=level,
            name=f"Воин {name}",
            magical_level=level,
            max_hp=70 * level,
            atk=25 * level,
            defens=10 * level,
            money=15)

class Wizard(Player):
    def __init__(self, level, name):
        class_info = "Волшебник"
        super().__init__(
            level=level,
            name=f"Волшебник {name}",
            magical_level=level,
            max_hp=60 * level,
            atk=17 * level,
            defens=5 * level,
            money=12)

class Monk(Player):
    def __init__(self, level, name):
        class_info = "Монах "
        super().__init__(
            level=level,
            name=f"Монах {name}",
            magical_level=level,
            max_hp=50 * level,
            atk=40 * level,
            defens=6 * level,
            money=8)

class Paladin(Player):
    def __init__(self, level, name):
        class_info = "Паладин"
        super().__init__(
            level=level,
            name=f"Паладин {name}",
            magical_level=level,
            max_hp=80 * level,
            atk=30 * level,
            defens=18 * level,
            money=30)

class Shop():
    def __init__(self):
        self.showcase = {"зелье": 20, "хлеб": 2,"гримуар": 50}

    def show_showcase(self):
        print("Ветрина: ")
        for key, value in self.showcase.items():
            print(f"| {key} = {value}")

    def sell(self, player, purchases):
        expenses = 0
        new_items = {}
        player_money = player.money
        for i in purchases:
            product = i
            if product in self.showcase:
                price = int(self.showcase[str(product)])
                expenses = expenses + price
                new_items.update({product: price})
            else:
                print("Shop.NO_PURCH_DATA")
        player.money = player_money-expenses
        player.inventory.update(new_items)
        return [player.money, player.inventory]

    def buy(self):
        pass





class Monster():
    def __init__(self,loot, level,name,magical_level, max_hp,atk,defens):
        self.level = level
        self.name = name
        self.magical_level = magical_level
        self.max_hp = max_hp
        self.hp = max_hp
        self.atk = atk
        self.defens = defens
        self.loot = loot

    def attack(self, oponent, defens_bool, coef):
        if defens_bool != 0:
            damage = self.atk*coef-oponent.defens
            if damage<0:
                oponent.hp = oponent.hp + damage
                return [round(oponent.hp, 2), -(damage)]
            else:
                oponent.hp = oponent.hp - damage
                return [round(oponent.hp, 2), damage]
        else:
            damage = self.atk*coef
            oponent.hp = oponent.hp - damage
            return [round(oponent.hp, 2), damage]

    def healing(self):
        healing_hp = self.hp + 30
        if healing_hp > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp = self.hp + 30
        return round(self.hp, 2)

    def defensing(self):
        return 1

    def player_looting(self, player):
        got_loot = {}
        moster_loot = self.loot
        money_count = 0
        for i in moster_loot:
            item = i
            chanse = moster_loot[item][1]
            probil = float(random.random())
            if moster_loot[item][0] != 1:
                if item == "монеты":
                    if probil <= chanse:
                        loot_count_coef = random.randint(1, 100)
                        loot_count = int((moster_loot[item][0]*(loot_count_coef/100))//1)
                        player.money = player.money + loot_count
                        money_count = loot_count
                    else:
                        pass
                else:
                    if probil <= chanse:
                        loot_count_coef = random.randint(1, 100)
                        loot_count = int((moster_loot[item][0]*(loot_count_coef/100))//1)
                        if loot_count !=0:
                            got_loot.update({item: loot_count})
                        else:
                            pass
                    else:
                        pass
            else:
                if probil >= chanse:
                    loot_count = 1
                    got_loot.update({item: loot_count})
                else:
                    pass
        player.inventory.update(got_loot)
        return [got_loot, player.inventory, money_count]






class Sceleton(Monster):
    monster_info = "Скелет"
    def __init__(self, level):
        super().__init__(
            level=level,
            name=f"Скелет ({level})",
            magical_level=level,
            max_hp=1*level,
            atk=16*level,
            defens=5*level,
            loot = {"монеты": [10, 0.7], "кости": [40, 1], "череп": [1, 0.3]})



class Dragon(Monster):
    def __init__(self, level):
        monster_info = "Дракон"
        super().__init__(
            level=level,
            name=f"Дракон ({level})",
            magical_level=level,
            max_hp=350*level,
            atk=61*level,
            defens=32*level,
            loot = {"монеты": [10, 0.7], "кости": [40, 1], "череп": [1, 0.3]})

class Cultist(Monster):
    def __init__(self, level):
        monster_info = "Культист"
        super().__init__(
            level=level,
            name=f"Культист ({level})",
            magical_level=level,
            max_hp=78*level,
            atk=30*level,
            defens=0*level,
            loot = {"монеты": [10, 0.7], "кости": [40, 1], "череп": [1, 0.3]})

class Drow(Monster):
    def __init__(self, level):
        monster_info = "Дроу"
        super().__init__(
            name=f"Дроу ({level})",
            level=level,
            magical_level=level,
            max_hp=85*level,
            atk=18*level,
            defens=30*level,
            loot = {"монеты": [10, 0.7], "кости": [40, 1], "череп": [1, 0.3]})

class Smoke_Mephit(Monster):
    def __init__(self, level):
        monster_info = "Дымный мефит"
        super().__init__(
            name=f"Дымный мефит ({level})",
            level=level,
            magical_level=level,
            max_hp=100*level,
            atk=24*level,
            defens=18*level,
            loot = {"монеты": [10, 0.7], "кости": [40, 1], "череп": [1, 0.3]})

class Babau(Monster):
    def __init__(self, level):
        monster_info = "Бабау"
        super().__init__(
            name=f"Бабау ({level})",
            level=level,
            magical_level= level,
            max_hp=70*level,
            atk=20*level,
            defens=10*level,
            loot = {"монеты": [10, 0.7], "кости": [40, 1], "череп": [1, 0.3]})

class Bone_Naga_Spirit(Monster):
    def __init__(self, level):
        monster_info = "Костяной Нага Дух"
        super().__init__(
            name=f"Костяной Нага Дух ({level})",
            level=level,
            magical_level=level,
            max_hp=70*level,
            atk=20*level,
            defens=10*level,
            loot = {"монеты": [10, 0.7], "кости": [40, 1], "череп": [1, 0.3]})




sceleton = Sceleton(1)
cultist = Cultist(1)
babau = Babau(1)
bone_naga_spirit = Bone_Naga_Spirit(1)
drow = Drow(1)
smoke_merhit = Smoke_Mephit(1)
dragon = Dragon(1)
# __________
shop = Shop()


all_monsters_list = [sceleton, cultist, babau, bone_naga_spirit, dragon,drow, smoke_merhit]
# cultist, babau, bone_naga_spirit, dragon,drow, smoke_merhit


def kubik(kubiks_edges = 25):
    kubik_val = random.randint(1,kubiks_edges)
    kubik_koef= round((kubik_val/kubiks_edges),1)
    return kubik_koef

def new_player_create():
    player_name = str(input("Создание игрока, ввидите имя: "))
    choise_class = int(input("Выберите класс: \n- Воин (1)\n- Волшебник (2)\n- Монах (3)"
                             "\n- Паладин (4)\n >"))
    if choise_class == 1:
        Player = Warrior(1, player_name)
    elif choise_class == 2:
        Player = Wizard(1, player_name)
    elif choise_class == 3:
        Player = Monk(1, player_name)
    elif choise_class == 4:
        Player = Paladin(1, player_name)
    else:
        Player = Warrior(1, player_name)
    return Player

def battle(player):
    player_defensing = 0
    oponent_defensing = 0
    oponent = all_monsters_list[random.randint(0,(len(all_monsters_list))-1)]
    print(f"Ваш опонент: {oponent.name}")
    time.sleep(1)

    while True:

        oponent_defensing = 0
        oponent_action = random.randint(0, 2)


        if oponent_action == 0:
            oponent_coef = kubik()
            print(f"Кубик: {oponent_coef}")
            attack_inf = oponent.attack(player, player_defensing,oponent_coef)
            print(f"Враг нанес вам {attack_inf[1]} урона, у вас осталось {attack_inf[0]} HP")

        elif oponent_action == 1:

            oponent_defensing = oponent.defensing()
            print(f"Враг защитился")

        elif oponent_action == 2:
            oponent.healing()
            print(f"Враг вылечился, HP сейчас: {oponent.hp}")

        print("_____________________")

        if player.hp <= 0:
            print(f"{oponent.name}, победил!")
            print("_____________________")
            break

        elif oponent.hp <= 0:
            print(f"{player.name}, победил!")
            looting_data = oponent.player_looting(player)
            print(f"{player.name} получил: {looting_data[0]}.\n Инвентарь сейчас: {looting_data[1]}, монеты: {player.money} + ({looting_data[2]}) \n_____________________")
            break



        time.sleep(1)

        player_defensing = 0
        print("Выберите действие:")
        action = str(input("Атаковать - A\n"
                           "Защищатся - D\n"
                           "Лечится - H: "))

        print("_____________________")


        if action =="A":
            player_coef = kubik()
            print(f"Кубик: {player_coef}")
            attack_inf = player.attack(oponent, oponent_defensing,player_coef)
            print(f"Вы нанесли врагу {attack_inf[1]} урона, у врага осталось {attack_inf[0]} HP")

        elif action =="D":
            player_defensing = player.defensing()
            print(f"Вы защитились")

        elif action == "H":
            player.healing()
            print(f"Вы вылечились, HP сейчас: {player.hp}")

        print("_____________________")

        if player.hp < 0:
            print(f"{oponent.name}, победил! \n_____________________")
            break

        elif oponent.hp < 0:
            print(f"{player.name}, победил!")
            looting_data = oponent.player_looting(player)
            print(f"{player.name} получил: {looting_data[0]}.\n Инвентарь сейчас: {looting_data[1]}, монеты: {player.money} + ({looting_data[2]}) \n_____________________")
            break

def shoping(player,shop):
    while True:
        shop_select = str(input("Приветствуем в магазине.\n"
              "B - Купить\n"
              "S - продать\n"
              "Q - Вернуться\n"
              ">"))
        if shop_select == "B":
            purchases_list=[]
            print(f"Что бы вы хотели приобрести?")
            print(f"Монеты: {player.money}")
            shop.show_showcase()
            while True:
                purchases_select = str(input("(Введите название или выйдете - Q) >"))
                if purchases_select != "Q":
                    purchases_list.append(purchases_select)
                else:
                    if purchases_list != []:
                        sell_data = shop.sell(player,purchases_list)
                        print(f"Монеты игрока: {sell_data[0]}, инвентарь: {sell_data[1]}")
                    else:
                        pass
                    break
        elif shop_select == "S":
            pass
        elif shop_select == "Q":
            break
        else:
            pass


def main(start):

    if start == 1:
        print("Приветствуем вас в мире меча и магии!")
        main_Player = new_player_create()
        start=0
    while True:
        main_select = str(input("Хотите сразится, или выйти из игры \n"
                                "A - Cражение\n"
                                "S - Магазин\n"
                                "I - Инвентарь\n"
                                "Q - Выход\n"
                                ">"))
        if main_select == "A":
            if main_Player.hp <= 0:
                print("Ваше здоровье низкое, вы не можете вступить в бой.")
            else:
                battle(main_Player)
        elif main_select == "S":
            shoping(main_Player, shop)
        elif main_select == "I":
            main_Player.see_inventory()
        elif main_select == "Q":
            break
        else:
            pass

if __name__ == '__main__':
    start=1
    main(start)
