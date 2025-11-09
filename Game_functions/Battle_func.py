from OOP_DnD_like_game.Game_functions.Kubic_func import *
from OOP_DnD_like_game.Assets import *
import time


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
            inventory_data = player.open_inventory()
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
