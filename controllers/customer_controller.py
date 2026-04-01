from controllers.user_controller import Uc
from models.menu import Mm
class customer_controller:
    uid=int(input("Enter user ID:"))
    if uid in Uc.U_name:
        Mm.menu()
    else:
        print("User Id does not exist")