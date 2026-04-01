from models.customer import customer


class CustomerRepository:
    
    def __init__(self):
        self.customers = {}
    
    def create_customer(self, c_id, c_name, c_phone, c_address, c_email):
        if c_id in self.customers:
            raise ValueError(f"Customer with ID {c_id} already exists")
        
        cust = customer(c_name, c_id, c_address, c_email, c_phone)
        self.customers[c_id] = cust
        return cust
    
    def get_customer_by_id(self, c_id):
        return self.customers.get(c_id)
    
    def get_customer_by_name(self, c_name):
        for cust in self.customers.values():
            if cust.c_name == c_name:
                return cust
        return None
    
    def get_all_customers(self):
        return list(self.customers.values())
    
    def update_customer(self, c_id, **kwargs):
        if c_id not in self.customers:
            raise ValueError(f"Customer with ID {c_id} not found")
        
        cust = self.customers[c_id]
        for key, value in kwargs.items():
            if hasattr(cust, key):
                setattr(cust, key, value)
        return cust
    
    def delete_customer(self, c_id):
        if c_id not in self.customers:
            raise ValueError(f"Customer with ID {c_id} not found")
        
        return self.customers.pop(c_id)
    
    def customer_exists(self, c_id):
        return c_id in self.customers
