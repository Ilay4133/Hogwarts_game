
class Shop:
    def __init__(self):
        self.showcase = {"зелье": {"стоимость": 20, "описание": "Восстанавливает 30 HP", 'type':  ['heal', 30]},
                         "хлеб": {"стоимость": 2, "описание": "Восстанавливает 3 HP", 'type': ['heal', 3]},
                         "гримуар": {"стоимость": 50, "описание": "Добавляет 20 урона на ход", 'type':  ['dmg_up', 20]},
                         "мифическое яблоко": {"стоимость": 999, "описание": "Увеличивает уровень игрока на 20 единиц",
                                               'type': ['lvl_up', 20]}}

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
                            pass
                        else:
                            self.showcase.update({item: player.inventory[item]})
                            self.showcase[item]["количество"] = count
                        del player.inventory[item]
                    else:
                        player.inventory[item]["количество"] -= count
                        if item in self.showcase:
                            pass
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
