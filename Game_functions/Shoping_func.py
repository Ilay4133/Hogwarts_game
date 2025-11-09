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
