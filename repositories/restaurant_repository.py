"""Restaurant Repository - Handles restaurant data persistence and retrieval"""
from models.restaurant import restaurant


class RestaurantRepository:
    """Repository for managing restaurant data"""
    
    def __init__(self):
        self.restaurants = {} 
    
    def create_restaurant(self, r_id, r_name, r_address, r_phone, r_ratings, r_status):
        """Create and store a new restaurant"""
        if r_id in self.restaurants:
            raise ValueError(f"Restaurant with ID {r_id} already exists")
        
        rest = restaurant(r_name, r_id, r_address, r_ratings, r_phone, r_status)
        self.restaurants[r_id] = rest
        return rest
    
    def get_restaurant_by_id(self, r_id):
        """Get restaurant by ID"""
        return self.restaurants.get(r_id)
    
    def get_restaurant_by_name(self, r_name):
        """Get restaurant by name"""
        for rest in self.restaurants.values():
            if rest.r_name == r_name:
                return rest
        return None
    
    def get_all_restaurants(self):
        """Get all restaurants"""
        return list(self.restaurants.values())
    
    def get_restaurants_by_rating(self, min_rating=0):
        """Get restaurants with rating >= min_rating"""
        return [r for r in self.restaurants.values() if r.r_ratings >= min_rating]
    
    def update_restaurant(self, r_id, **kwargs):
        """Update restaurant attributes"""
        if r_id not in self.restaurants:
            raise ValueError(f"Restaurant with ID {r_id} not found")
        
        rest = self.restaurants[r_id]
        for key, value in kwargs.items():
            if hasattr(rest, key):
                setattr(rest, key, value)
        return rest
    
    def delete_restaurant(self, r_id):
        """Delete restaurant by ID"""
        if r_id not in self.restaurants:
            raise ValueError(f"Restaurant with ID {r_id} not found")
        
        return self.restaurants.pop(r_id)
    
    def restaurant_exists(self, r_id):
        """Check if restaurant exists"""
        return r_id in self.restaurants
