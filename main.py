

from repositories import (
    UserRepository,
    CustomerRepository,
    RestaurantRepository,
    OrderRepository,
    FoodRepository
)
from controllers.user_controller import user_controller


class FoodDeliveryApp:
    
    def __init__(self):
        self.user_repo = UserRepository()
        self.customer_repo = CustomerRepository()
        self.restaurant_repo = RestaurantRepository()
        self.order_repo = OrderRepository()
        self.food_repo = FoodRepository()
    
    def register_customer_menu(self):
        print("\n" + "="*50)
        print("CUSTOMER REGISTRATION")
        print("="*50)
        
        try:
            name = input("Enter customer name: ").strip()
            c_id = int(input("Enter customer ID: "))
            phone = input("Enter phone number (10 digits): ").strip()
            address = input("Enter address: ").strip()
            email = input("Enter email: ").strip()
            
            if len(phone) != 10 or not phone.isdigit():
                print("Phone number must be 10 digits!")
                return
            
            if '@' not in email:
                print("Invalid email format!")
                return
            
            customer = user_controller.register_customer(
                name, c_id, int(phone), address, email
            )
            
            print(f"Customer registered successfully!")
            print(f"   Name: {customer.u_name}, ID: {customer.u_id}")
            
        except ValueError as e:
            print(f" Error: {e}")
        except Exception as e:
            print(f" Unexpected error: {e}")
    
    def register_restaurant_menu(self):
        print("\n" + "="*50)
        print("RESTAURANT REGISTRATION")
        print("="*50)
        
        try:
            name = input("Enter restaurant name: ").strip()
            r_id = int(input("Enter restaurant ID: "))
            phone = input("Enter phone number (10 digits): ").strip()
            address = input("Enter restaurant address: ").strip()
            email = input("Enter email: ").strip()
            
            if len(phone) != 10 or not phone.isdigit():
                print(" Phone number must be 10 digits!")
                return
            
            if '@' not in email:
                print(" Invalid email format!")
                return
            
            restaurant = user_controller.register_restaurent(
                name, r_id, int(phone), address, email
            )
            
            print(f" Restaurant registered successfully!")
            print(f"   Name: {restaurant.u_name}, ID: {restaurant.u_id}")
            
        except ValueError as e:
            print(f" Error: {e}")
        except Exception as e:
            print(f" Unexpected error: {e}")
    
    def add_food_menu(self):
        print("\n" + "="*50)
        print("ADD FOOD ITEM")
        print("="*50)
        
        try:
            f_id = int(input("Enter food ID: "))
            f_name = input("Enter food name: ").strip()
            f_type = input("Enter food type (e.g., Veg/Non-Veg): ").strip()
            f_prize = float(input("Enter food price: "))
            
            food_item = self.food_repo.create_food(f_id, f_name, f_type, f_prize)
            print(f"Food item added successfully!")
            print(f"   Name: {food_item.f_name}, Price: ${food_item.f_prize}")
            
        except ValueError as e:
            print(f" Error: {e}")
        except Exception as e:
            print(f" Unexpected error: {e}")
    
    def place_order_menu(self):
        print("\n" + "="*50)
        print("PLACE ORDER")
        print("="*50)
        
        try:
            o_id = int(input("Enter order ID: "))
            o_time = input("Enter order time (HH:MM): ").strip()
            o_type = input("Enter order type (Delivery/Dine-in): ").strip()
            
            order = self.order_repo.create_order(o_id, o_time, o_type)
            print(f" Order placed successfully!")
            print(f"   Order ID: {order.o_id}, Type: {order.o_type}, Time: {order.o_time}")
            
        except ValueError as e:
            print(f" Error: {e}")
        except Exception as e:
            print(f" Unexpected error: {e}")
    
    def view_all_users(self):
        print("\n" + "="*50)
        print("ALL REGISTERED USERS")
        print("="*50)
        
        all_users = self.user_repo.get_all_users()
        if not all_users:
            print("No users registered yet.")
            return
        
        for user in all_users:
            print(f"\nID: {user.u_id}")
            print(f"Name: {user.u_name}")
            print(f"Phone: {user.u_phone}")
            print(f"Email: {user.u_email}")
            print(f"Address: {user.u_address}")
            print(f"Type: {user.u_type}")
            print("-" * 50)
    
    def view_all_foods(self):
        print("\n" + "="*50)
        print("ALL FOOD ITEMS")
        print("="*50)
        
        all_foods = self.food_repo.get_all_foods()
        if not all_foods:
            print("No food items added yet.")
            return
        
        for f in all_foods:
            print(f"\nID: {f.f_id}")
            print(f"Name: {f.f_name}")
            print(f"Type: {f.f_type}")
            print(f"Price: ${f.f_prize}")
            print("-" * 50)
    
    def view_all_orders(self):
        print("\n" + "="*50)
        print("ALL ORDERS")
        print("="*50)
        
        all_orders = self.order_repo.get_all_orders()
        if not all_orders:
            print("No orders placed yet.")
            return
        
        for ord in all_orders:
            print(f"\nOrder ID: {ord.o_id}")
            print(f"Time: {ord.o_time}")
            print(f"Type: {ord.o_type}")
            print("-" * 50)
    
    def main_menu(self):
        while True:
            print("\n" + "="*50)
            print(" FOOD DELIVERY SYSTEM ")
            print("="*50)
            print("1. Register Customer")
            print("2. Register Restaurant")
            print("3. Add Food Item")
            print("4. Place Order")
            print("5. View All Users")
            print("6. View All Food Items")
            print("7. View All Orders")
            print("8. Exit")
            print("="*50)
            
            choice = input("Enter your choice (1-8): ").strip()
            
            if choice == '1':
                self.register_customer_menu()
            elif choice == '2':
                self.register_restaurant_menu()
            elif choice == '3':
                self.add_food_menu()
            elif choice == '4':
                self.place_order_menu()
            elif choice == '5':
                self.view_all_users()
            elif choice == '6':
                self.view_all_foods()
            elif choice == '7':
                self.view_all_orders()
            elif choice == '8':
                print("\n Thank you for using Food Delivery System!")
                print("Goodbye!")
                break
            else:
                print(" Invalid choice! Please enter 1-8.")


def main():
    app = FoodDeliveryApp()
    app.main_menu()


if __name__ == '__main__':
    main()
