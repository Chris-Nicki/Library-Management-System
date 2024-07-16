# ======== Book Class ======== #

class Book():
    def __init__(self, isbn, title, author, pub_date, genre, fiction ):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.pub_date = pub_date
        self.genre = genre
        self.fiction = fiction
        self.is_available = True 
 
        
    def get_title(self):
        return self.title
        
    def in_stock(self):
        return self.is_available
            
    def get_isbn(self):
        return self.isbn
        
        
    def get_author(self):
        return self.author

    def set_is_available(self, availability):
            self.is_available = availability


    def checkout_book(self):
        if self.is_available:
            self.is_available(False)
            return True
        else:
            return False

    def check_in(self):
            self.is_available(True)

