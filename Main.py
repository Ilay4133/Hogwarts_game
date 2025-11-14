from Game_functions.Battle_func import *
from Game_functions.Shoping_func import *
from Game_functions.New_player_create_func import *
from Assets import *


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
            if main_Player.hp <= main_Player.max_hp:
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
