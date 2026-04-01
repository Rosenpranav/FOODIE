
from models.user import User


class UserRepository:
    
    def __init__(self):
        self.users = {} 
    
    def create_user(self, u_id, u_name, u_phone, u_address, u_email, u_type):
        """Create and store a new user"""
        if u_id in self.users:
            raise ValueError(f"User with ID {u_id} already exists")
        
        user = User(u_id, u_name, u_phone, u_address, u_email, u_type)
        self.users[u_id] = user
        User.U_name.append(u_name)
        User.U_id.append(u_id)
        return user
    
    def get_user_by_id(self, u_id):
        """Get user by ID"""
        return self.users.get(u_id)
    
    def get_user_by_name(self, u_name):
        """Get user by name"""
        for user in self.users.values():
            if user.u_name == u_name:
                return user
        return None
    
    def get_all_users(self):
        """Get all users"""
        return list(self.users.values())
    
    def update_user(self, u_id, **kwargs):
        """Update user attributes"""
        if u_id not in self.users:
            raise ValueError(f"User with ID {u_id} not found")
        
        user = self.users[u_id]
        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
        return user
    
    def delete_user(self, u_id):
        """Delete user by ID"""
        if u_id not in self.users:
            raise ValueError(f"User with ID {u_id} not found")
        
        user = self.users.pop(u_id)
        if user.u_name in User.U_name:
            User.U_name.remove(user.u_name)
        if u_id in User.U_id:
            User.U_id.remove(u_id)
        return user
    
    def user_exists(self, u_id):
        """Check if user exists"""
        return u_id in self.users
