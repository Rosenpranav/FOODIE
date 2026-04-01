class User:
    U_name = []
    U_id = []

    def __init__(self, u_id, u_name, u_phone, u_address, u_email, u_type):
        self.u_id = u_id
        self.u_name = u_name
        self.u_address = u_address
        self.u_phone = u_phone
        self.u_email = u_email
        self.u_type = u_type

    def __repr__(self):
        return f"User(id={self.u_id}, name={self.u_name}, type={self.u_type})"