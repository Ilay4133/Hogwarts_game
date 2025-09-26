import random

class Wizard():
    def __init__(self,name,magical_level, max_hp,atk,defens):
        self.name = name
        self.magical_level = magical_level
        self.max_hp = max_hp
        self.hp = max_hp
        self.atk = atk
        self.defens = defens
        self.faculty = None

    def attack(self, oponent):
        oponent.hp = oponent.hp - self.atk
        return oponent.hp

    def healing(self):
        healing_hp = self.hp + 30
        if healing_hp > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp = self.hp + 30
        return self.hp



class Harry_Potter(Wizard):
    def __init__(self):
        magical_level = 4
        super().__init__(
            name = "Гарри Поттер",
            magical_level= magical_level,
            max_hp = 50*magical_level,
            atk=20*magical_level,
            defens = 5*magical_level)

class Wolan_De_Mort(Wizard):
    def __init__(self):
        magical_level = 6
        super().__init__(
            name = "Волан Де Морт",
            magical_level = magical_level,
            max_hp = 50*magical_level,
            atk=20*magical_level,
            defens = 5*magical_level)

class Albus_Daambldor(Wizard):
    def __init__(self):
        magical_level = 7
        super().__init__(
            name = "Альбус Дамблдор",
            magical_level= magical_level,
            max_hp = 50*magical_level,
            atk=20*magical_level,
            defens = 5*magical_level)

class Sevirus_Sneg(Wizard):
    def __init__(self):
        magical_level = 5
        super().__init__(
            name = "Севиус Снег",
            magical_level= magical_level,
            max_hp = 50*magical_level,
            atk=20*magical_level,
            defens = 5*magical_level)


#all_wizards_name_list = [harry]
#all_wizards_class_list = [Harry_Potter,Wolan_De_Mort,Albus_Daambldor,Sevirus_Sneg]
# def create_all_wizards_list(names,classes):
#     all_wizards_list = []
#     for i in range(len(names)):
#         name = names[i]
#         clas = classes[i]
#         all_wizards_list.append()


harry_potter = Harry_Potter()
wolan_de_mort = Wolan_De_Mort()

all_wizards_list = [harry_potter,wolan_de_mort]




def new_player_create():
    player_name = str(input("Создание игрока, ввидите имя: "))
    Player = Wizard(player_name,4,600,50,45)
    return Player

def battle(player):
    oponent = all_wizards_list[random.randint(0,(len(all_wizards_list))-1)]
    print(oponent.name)

    while oponent.hp > 0:
        print("Выберите действие:")
        action = str(input("Атаковать - A\n"
                           "Защищатся - D\n"
                           "Лечится - H: "))
        if action =="A":
            player.attack(oponent)
            print(f"Вы нанесли врагу {player.atk} урона, у врага осталось {oponent.hp} HP")

        elif action == "H":
            player.healing()
            print(f"Вы вылечились, HP сейчас: {player.hp}")
    print(f"{player.name}, победил!")


def main():
    print("Приветствуем вас в мире магии!")
    Main_Player = new_player_create()
    while True:
        select_test = str(input("Хотите сразится, или выйти из игры (A - сражение, Q - выход):"))
        if select_test == "A":
            battle(Main_Player)
        elif select_test == "Q":
            break

if __name__ == '__main__':
    main()
