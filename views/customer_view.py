from controllers.customer_controller import Cc
class customer_view:
    print("1.Place order")
    print("2.Cancel order")
    print("3.Show menu") 
    cho=int(input("Enter choice:"))
    if cho==1:
        Cc.place_order()
    if cho==2:
        Cc.cancel_order()
    if cho==3:
        Cc.show_menu()
