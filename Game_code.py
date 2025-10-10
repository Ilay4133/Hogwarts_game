import random
import time
class Wizard():
    def __init__(self,name,magical_level, max_hp,atk,defens):
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



class Harry_Potter(Wizard):
    def __init__(self):
        magical_level = 4
        super().__init__(
            name = "Гарри Поттер",
            magical_level= magical_level,
            max_hp = 70*magical_level,
            atk=20*magical_level,
            defens = 10*magical_level)

class Wolan_De_Mort(Wizard):
    def __init__(self):
        magical_level = 6
        super().__init__(
            name = "Волан Де Морт",
            magical_level = magical_level,
            max_hp = 70*magical_level,
            atk=20*magical_level,
            defens = 10*magical_level)

class Albus_Daambldor(Wizard):
    def __init__(self):
        magical_level = 7
        super().__init__(
            name = "Альбус Дамблдор",
            magical_level= magical_level,
            max_hp = 70*magical_level,
            atk=20*magical_level,
            defens = 10*magical_level)

class Sevirus_Sneg(Wizard):
    def __init__(self):
        magical_level = 5
        super().__init__(
            name = "Севирус Снег",
            magical_level= magical_level,
            max_hp = 70*magical_level,
            atk=20*magical_level,
            defens = 10*magical_level)


harry_potter = Harry_Potter()
wolan_de_mort = Wolan_De_Mort()
albus_dambldor = Albus_Daambldor()
sevirus_sneg = Sevirus_Sneg()

all_wizards_list = [harry_potter,wolan_de_mort,albus_dambldor,sevirus_sneg]


def kubik(kubiks_edges = 25):
    kubik_val = random.randint(1,kubiks_edges)
    kubik_koef= round((kubik_val/kubiks_edges),2)
    return kubik_koef

def new_player_create():
    player_name = str(input("Создание игрока, ввидите имя: "))
    Player = Wizard(player_name,4,280,80,40)
    return Player

def battle(player):
    player_defensing = 0
    oponent_defensing = 0
    oponent = all_wizards_list[random.randint(0,(len(all_wizards_list))-1)]
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

        if player.hp < 0:
            print(f"{oponent.name}, победил!")
            print("_____________________")
            break

        elif oponent.hp < 0:
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
