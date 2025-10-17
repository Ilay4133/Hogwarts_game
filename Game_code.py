import random
import time

class Player():
    def __init__(self,level,name,magical_level, max_hp,atk,defens):
        self.level = level
        self.name = name
        self.magical_level = magical_level
        self.max_hp = max_hp
        self.hp = max_hp
        self.atk = atk
        self.defens = defens
        self.inventory = {}

    def attack(self, oponent, defens_bool, coef):
        if defens_bool != 0:
            damage = self.atk-oponent.defens*coef
            oponent.hp = oponent.hp - damage
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

class Warrior(Player):
    def __init__(self, level, name):
        class_info = "Воин"
        super().__init__(
            level=level,
            name=f"Воин {name}",
            magical_level=level,
            max_hp=70 * level,
            atk=25 * level,
            defens=10 * level)

class Wizard(Player):
    def __init__(self, level, name):
        class_info = "Волшебник"
        super().__init__(
            level=level,
            name=f"Волшебник {name}",
            magical_level=level,
            max_hp=60 * level,
            atk=17 * level,
            defens=5 * level)

class Monk(Player):
    def __init__(self, level, name):
        class_info = "Монах "
        super().__init__(
            level=level,
            name=f"Монах {name}",
            magical_level=level,
            max_hp=50 * level,
            atk=40 * level,
            defens=6 * level)

class Paladin(Player):
    def __init__(self, level, name):
        class_info = "Паладин"
        super().__init__(
            level=level,
            name=f"Паладин {name}",
            magical_level=level,
            max_hp=80 * level,
            atk=30 * level,
            defens=18 * level)

class Monster():
    def __init__(self,level,name,magical_level, max_hp,atk,defens):
        self.level = level
        self.name = name
        self.magical_level = magical_level
        self.max_hp = max_hp
        self.hp = max_hp
        self.atk = atk
        self.defens = defens

    def attack(self, oponent, defens_bool, coef):
        if defens_bool != 0:
            damage = self.atk-oponent.defens*coef
            oponent.hp = oponent.hp - damage
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



class Sceleton(Monster):
    def __init__(self, level):
        class_info = "Скелет"
        super().__init__(
            level=level,
            name=f"Скелет ({level})",
            magical_level=level,
            max_hp=55*level,
            atk=16*level,
            defens=5*level)

class Dragon(Monster):
    def __init__(self, level):
        class_info = "Дракон"
        super().__init__(
            level=level,
            name=f"Дракон ({level})",
            magical_level=level,
            max_hp=350*level,
            atk=61*level,
            defens=32*level)

class Cultist(Monster):
    def __init__(self, level):
        class_info = "Культист"
        super().__init__(
            level=level,
            name=f"Культист ({level})",
            magical_level=level,
            max_hp=78*level,
            atk=30*level,
            defens=0*level)

class Drow(Monster):
    def __init__(self, level):
        class_info = "Дроу"
        super().__init__(
            name=f"Дроу ({level})",
            level=level,
            magical_level=level,
            max_hp=85*level,
            atk=18*level,
            defens=30*level)

class Smoke_Mephit(Monster):
    def __init__(self, level):
        class_info = "Дымный мефит"
        super().__init__(
            name=f"Дымный мефит ({level})",
            level=level,
            magical_level=level,
            max_hp=100*level,
            atk=24*level,
            defens=18*level)

class Babau(Monster):
    def __init__(self, level):
        class_info = "Бабау"
        super().__init__(
            name=f"Бабау ({level})",
            level=level,
            magical_level= level,
            max_hp=70*level,
            atk=20*level,
            defens=10*level)

class Bone_Naga_Spirit(Monster):
    def __init__(self, level):
        class_info = "Костяной Нага Дух"
        super().__init__(
            name=f"Костяной Нага Дух ({level})",
            level=level,
            magical_level=level,
            max_hp=70*level,
            atk=20*level,
            defens=10*level)

sceleton = Sceleton(1)
cultist = Cultist(1)
babau = Babau(1)
bone_naga_spirit = Bone_Naga_Spirit(1)
drow = Drow(1)
smoke_merhit = Smoke_Mephit(1)
dragon = Dragon(1)


all_monsters_list = [sceleton, cultist, babau, bone_naga_spirit, dragon,
                     drow, smoke_merhit]

def kubik(kubiks_edges = 25):
    kubik_val = random.randint(1,kubiks_edges)
    kubik_koef= round((kubik_val/kubiks_edges),2)
    return kubik_koef

def new_player_create():
    player_name = str(input("Создание игрока, ввидите имя: "))
    choise_class = int(input("Выберите класс: \n- Воин (1)\n- Волшебник (2)\n- Монах (3)"
                             "\n- Паладин (4):"))
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
            print("_____________________")
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
            print(f"{player.name}, победил! \n_____________________")
            break



def main():
    print("Приветствуем вас в мире меча и магии!")
    Main_Player = new_player_create()
    while True:
        select_test = str(input("Хотите сразится, или выйти из игры (A - сражение, Q - выход):"))
        if select_test == "A":
            battle(Main_Player)
        elif select_test == "Q":
            break

if __name__ == '__main__':
    main()
