from models.user import User

class user_controller:
    def register_customer(name, u_id, phone, address, email):
        if len(str(phone)) != 10:
            raise ValueError("Enter correct phone number !!")
        if '@' not in email:
            raise ValueError("Enter correct email !!")

        customer = User(u_id, name, phone, address, email, 'customer')
        User.U_name.append(name)
        User.U_id.append(u_id)
        return customer

    def register_restaurent(name, u_id, phone, address, email):
        if len(str(phone)) != 10:
            raise ValueError("Enter correct phone number !!")
        if '@' not in email:
            raise ValueError("Enter correct email !!")

        restaurant = User(u_id, name, phone, address, email, 'restaurant')
        User.U_name.append(name)
        User.U_id.append(u_id)
        return restaurant


Uc = user_controller

if __name__ == '__main__':
    na = input("Enter user name:")
    uid = int(input("Enter an new userid:"))
    ph = int(input("Enter your phone Number:"))
    ty = input("Enter whether you are customer/restaurant")
    ad = input("Enter your address:")
    em = input("Enter your email:")

    if ty == "customer":
        user_controller.register_customer(na, uid, ph, ad, em)
    elif ty == "restaurant":
        user_controller.register_restaurent(na, uid, ph, ad, em)
    else:
        print("Invalid type")