
class User:
    def __init__(self, id_num, name, address, birthday):
        self.id_num = id_num
        self.name = name
        self. address = address
        self.birthday = birthday
        self.books_checked_out = []
    
    def get_id(self):
        return self.id_num

    def get_user(self):
        return self.name
        
    def get_birthday(self):
        return self.birthday
    
    def get_address(self):
        return self.address
    

    
