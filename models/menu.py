from models.order import Mo
class menu:
    print("1.Pizza")
    print("2.Burger")
    print("3.Chappathi")
    print("4.Dosa")
    print("5.Idli")
    men=input("Enter the menu:")
    print("Menu selected successfully !!")
    Mo.placeorder("Dosa")
    if men=="pizza":
        Mo.place_order("Pizza")
    if men=="burger":
        Mo.place_order("Burger")
    if men=="chappathi":
        Mo.place_order("Chappathi")
    if men=="dosa":
        Mo.place_order("Dosa")
    if men=="idli":
        Mo.place_order("Idli")