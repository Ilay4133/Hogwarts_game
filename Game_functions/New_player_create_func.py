from OOP_DnD_like_game.Classes.Player_classes.Warrior_class import *
from OOP_DnD_like_game.Classes.Player_classes.Wizard_class import *
from OOP_DnD_like_game.Classes.Player_classes.Monk_class import *
from OOP_DnD_like_game.Classes.Player_classes.Paladin_class import *


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
