from models.order import Mo
class user_view:
    print("Enter a choice:")
    print("1.CREATE USER")
    print("2.PLACE ORDER")
    print("3.CANCEL ORDER")
    print("4.GET LOCATION OF THE DELIVER AGENT")
    s=int(input())
    if s==3:
        Mo.cancel_order()
    if s==2:
        Mo.place_order()