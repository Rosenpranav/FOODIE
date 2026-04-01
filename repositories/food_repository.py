
from models.food import food


class FoodRepository:
    
    def __init__(self):
        self.foods = {}
    
    def create_food(self, f_id, f_name, f_type, f_prize):
        if f_id in self.foods:
            raise ValueError(f"Food with ID {f_id} already exists")
        
        food_item = food(f_id, f_name, f_type, f_prize)
        self.foods[f_id] = food_item
        return food_item
    
    def get_food_by_id(self, f_id):
        return self.foods.get(f_id)
    
    def get_food_by_name(self, f_name):
        for f in self.foods.values():
            if f.f_name == f_name:
                return f
        return None
    
    def get_all_foods(self):
        return list(self.foods.values())
    
    def get_foods_by_type(self, f_type):
        return [f for f in self.foods.values() if f.f_type == f_type]
    
    def get_foods_by_price_range(self, min_price, max_price):
        return [f for f in self.foods.values() if min_price <= f.f_prize <= max_price]
    
    def update_food(self, f_id, **kwargs):
        if f_id not in self.foods:
            raise ValueError(f"Food with ID {f_id} not found")
        
        food_item = self.foods[f_id]
        for key, value in kwargs.items():
            if hasattr(food_item, key):
                setattr(food_item, key, value)
        return food_item
    
    def delete_food(self, f_id):
        if f_id not in self.foods:
            raise ValueError(f"Food with ID {f_id} not found")
        
        return self.foods.pop(f_id)
    
    def food_exists(self, f_id):
        return f_id in self.foods
