
from models.order import order


class OrderRepository:
    
    def __init__(self):
        self.orders = {}
    def create_order(self, o_id, o_time, o_type):
        if o_id in self.orders:
            raise ValueError(f"Order with ID {o_id} already exists")
        
        ord = order(o_id, o_time, o_type)
        self.orders[o_id] = ord
        return ord
    
    def get_order_by_id(self, o_id):
        return self.orders.get(o_id)
    
    def get_all_orders(self):
        return list(self.orders.values())
    
    def get_orders_by_type(self, o_type):
        return [o for o in self.orders.values() if o.o_type == o_type]
    
    def update_order(self, o_id, **kwargs):
        if o_id not in self.orders:
            raise ValueError(f"Order with ID {o_id} not found")
        
        ord = self.orders[o_id]
        for key, value in kwargs.items():
            if hasattr(ord, key):
                setattr(ord, key, value)
        return ord
    
    def delete_order(self, o_id):
        if o_id not in self.orders:
            raise ValueError(f"Order with ID {o_id} not found")
        
        return self.orders.pop(o_id)
    
    def order_exists(self, o_id):
        return o_id in self.orders
