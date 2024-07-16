
from connect_sql import connect_database
from mysql.connector import Error
from books import Book
from genres import Genre
from author import Author
from users import User

class Library:

    def __init__(self):
        self.books = []  # stores instances of the Book class
        self.user = []
        self.author = []
        self.genre = []
        self.current_loans = {}

    # add a book object to self.books
    def add_book(self, book):
        try:
            conn = connect_database()
            cursor = conn.cursor()

            self.books.append(book)
            print(f"""{book.title}, by {book.author}:\nBook info:\nISBN: {book.isbn}, Publication Date:{book.pub_date}, {book.genre}, {book.fiction} has been added to the library.""")
            query = "INSERT INTO Books (isbn, title, author, genre, publication_Date, availability, fiction) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(query, (book.isbn, book.title, book.author, book.genre, book.pub_date, book.is_available, book.fiction))
            conn.commit()
            print("Book added!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()
    def all_books(self):
         print([book.title for book in self.books])

    # searching for a book
    def find_book(self, title):
         book = input("What book would you like to search?")
         for book in self.books:
            if book:
                availability = "available" if book.is_available else "not available"
                print(f"""{title}, by {book.author}, is {availability}. \n Book info:\n ISBN: {book.isbn}, Publication Date:{book.pub_date}, {book.genre}, {book.fiction}""")
            else:
                return None
    
        
    def lend_book(self, user):
        isbn = input("What is the isbn of the book you would like to check out? ")
        
        user = input("What is the users id?")

        if isbn in self.books and self.books[isbn].checkout_book():
            self.current_loans[isbn] = user 
         
            user.books_checked_out.append(self.books[isbn])
           
            print(f"Book {self.books[isbn].get_title()} checked out to {user}")
        else:
            print("That book is unavailable")

    def return_book(self):
        isbn = input("Enter ISBN of the book to return: ")
        if isbn in self.books and isbn in self.current_loans:
            self.books[isbn].return_book()
            del self.current_loans[isbn]
            print(f"Book {self.books[isbn].get_title()} was returned")

            


    def add_user(self,user):
        
        try:
            conn = connect_database()
            cursor = conn.cursor()

            self.user.append(user)
            
            query = "INSERT INTO users (library_id, name, address, birthday) VALUES (%s, %s,%s,%s)"
            cursor.execute(query, (user.id_num, user.name, user.address, user.birthday))
            conn.commit()
            print(f"{user.id_num} {user.name} added to users!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()
    
    def find_user(self,user_name):
        for user in self.user:
            if user.name ==  user_name:
                print(f"{user.name}, {user.address}, {user.birthday}")
        else:
            return None
    
    def all_users(self):
        print([user.name for user in self.user])
    

    def add_author(self, Author):
        self.author.append(Author)


    def find_author(self, author):
        author = input("What author would you like to search? ")
        for author in self.author:
            if author:
                print(f"Name:{author.name}, Birthday:{author.birthday},Birth Country:{author.birth_country}\n Biography:{author.biography}")
        else:
            return None
    
    def all_authors(self):
         print([author.name for author in self.author])
        
    def add_author(self, author):
        try:
            conn = connect_database()
            cursor = conn.cursor()

            self.author.append(author)
            
            query = "INSERT INTO authors (name, birthday, birth_country, biography) VALUES (%s, %s,%s,%s)"
            cursor.execute(query, (author.name, author.birthday, author.birth_country, author.biography))
            conn.commit()
            print(f"{author.name} added to authors!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

 


    def add_genre(self, genre):
        try:
            conn = connect_database()
            cursor = conn.cursor()

            self.genre.append(genre)
           
            query = "INSERT INTO genres (genre_name, genre_details) VALUES (%s, %s)"
            cursor.execute(query, (genre.genre, genre.description))
            conn.commit()
            print("Genre added!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()


    def find_genre(self):
        for genre in self.genre:
            if self.genre == genre:
                return genre
        else:
            return None

    def display_all(self):
        print([genre.genre for genre in self.genre])
