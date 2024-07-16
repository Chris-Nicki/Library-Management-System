# ========== Library Management System ============= #
"""Enhanced User Interface (UI) and Menu:

Create an improved, user-friendly command-line interface (CLI) for the 
Library Management System with separate menus for each class of the system.
```
Welcome to the Library Management System!
Main Menu:
1. Book Operations
2. User Operations
3. Author Operations
4. Genre Operations
5. Quit

```
"""

from books import Book
from library import Library
from users import User
from author import Author
from genres import Genre

import re
import random

library = Library()
def book_operations(library):
  
    print("Welcome to Book Operations")
    while True:
        print("""Book Operations Menu
1. Add a new book
2. Borrow a book
3. Return a book
4. Search for a book
5. Display all books
6. Back to main menu

""")
        book_op = input("What would you like to do? ").lower().strip()
        if book_op == "6":
            break

        try:
            if book_op == "1":
                while True:
                    isbn_entry = (input("Please enter the ISBN format ###-#-#-##-######-#: "))
                    isbn_pattern = re.compile(r"\d{3}-\d{1}-\d{1}-\d{2}-\d{5}-\d{1}")  
                    isbn_match = re.match(isbn_pattern, isbn_entry)
                    if isbn_match:
                        isbn = isbn_match.group() 
                        print("Valid ISBN:", isbn) 
                        break  
                    else:
                        print("Invalid ISBN format. Please try again.")  # Remove leading/trailing whitespace
                title = input("What is the title? ").lower().strip()
                author =input("Who is the author? ").lower().strip()
                while True: 
                    pub_date_entry = input("Please enter a Publication Date in the format DD/MM/YYYY (e.g., 01/01/2000): ").lower()
                    pub_date_pattern = re.compile(r"\d{2}/\d{2}/\d{4}")  
                    pub_date_match = re.match(pub_date_pattern, pub_date_entry)
                    if pub_date_match:
                        pub_date = pub_date_match.group(0)  
                        break  
                    else:
                        print("Invalid publication date format. Please try again.")
                genre = input("What is the genre?").lower().strip()
                fiction = input("Fiction, Non-Fiction, Reference ").lower().strip()
                book = Book(isbn, title, author, pub_date, genre, fiction)
                library.add_book(book)
                print(f"Added {title} to the library.")

            elif book_op == "2":
                library.lend_book(title) 
            elif book_op == "3":
                title = input("What would you book like to return?")
                library.return_book(title)
            elif book_op == "4":
                library.find_book(title)
            elif book_op == "5":
                library.all_books()
        except Exception as e:
            print(f"An error occurred: {e}")

      
        
def user_operations(library):
    print("Welcome to User Operations: ")
  
    while True:
        print("""User Operations Menu:
User Operations:
1. Add a new user
2. View user details
3. Display all users
4. Back to main menu
""")
        user_op = input("What would you like to do? ").lower().strip()
        if user_op == "4":
            break
        try:    
            if user_op == "1":
                
                id_nump =  random.randint(1,10000)
                id_nump = str(id_nump)
                id_num = id_nump
                name = input("What is your name? ").lower()
                address =input("What is your address? ").lower().strip()
                while True: 
                    birthday_entry = input("Please enter a birthday in the format DD/MM/YYYY (e.g., 01/01/2000): ").lower()
                    birthday_pattern = re.compile(r"\d{2}/\d{2}/\d{4}")  
                    birthday_match = re.match(birthday_pattern, birthday_entry)
                    if birthday_match:
                        birthday = birthday_match.group(0)  
                        break  
                    else:
                        print("Invalid birthday format. Please try again.")
                user = User(id_num, name, address, birthday)
                
                library.add_user(user)
            elif user_op == "2":
                user_name= input("What is the user name for the user details? ")
                print(library.find_user(user_name))
            elif user_op == "3":
                library.all_users()          
        except Exception as e:
            print(f"An error occurred: {e}")    

def author_operations(library):
    print("Welcome to Author Operations: ")

    while True:
        print("""Author Operations Menu:
Author Operations:
1. Add a new author
2. View author details
3. Display all authors
4. Back to main menu
""")
        author_op = input("What would you like to do? ")
        if author_op == "4":
            break
        try: 
            if author_op == "1":
                print("Lets add an Author to the database:")
                name = input("Please enter the author's name: ").lower().strip()

                while True:  # Input validation loop for birthday
                    birthday_entry = input("Please enter a birthday in the format DD/MM/YYYY (e.g., 01/01/2000): ").lower()
                    birthday_pattern = re.compile(r"\d{2}/\d{2}/\d{4}")  # Correct pattern for DD/MM/YYYY
                    birthday_match = re.match(birthday_pattern, birthday_entry)
                    if birthday_match:
                        birthday = birthday_match.group(0)  # Extract matched birthday string
                        break  # Exit the loop if a valid birthday is entered
                    else:
                        print("Invalid birthday format. Please try again.")
                birth_country = input("Please enter the author's birth country: ").lower().strip()
                biography = input("Please enter a biography for the author: ").lower().strip()
                author = Author(name, birthday, birth_country, biography)
                library.add_author(author)
            elif author_op == "2":
                library.find_author(author)
            elif author_op == "3":
                library.all_authors()
            elif author_op == "4":
                break   
            else:
                print("Please enter a valid input: ")
        except Exception as e:
            print(f"Error:{e}")

def genre_operations(library):
    print("Welcome to Genre Operations: ")
    while True:
        print("""Genre Operations Menu:
1. Add a new genre
2. View genre details
3. Display all genres
4. Back to main menu
""")
        genre_op = input("What would you like to do? ")
        if genre_op == "4":
            break
        try:
            if genre_op == "1":
                print("Let's add a genre!")
                genre = input("What is the Genre name? ").lower().strip()
                description = input("Please give a brief description of the genre:  ").lower().strip()
                genre = Genre( genre, description)
                library.add_genre(genre)
            elif genre_op == "2":
                library.find_genre()
            elif genre_op == "3":
                library.display_all()
            elif genre_op == "4":
                break
        except Exception as e:
            print(f"An error occurred: {e}")  
                    

def library_management_system():
    print("Welcome To The Library Management System ")
    
    while True:
            print("""Menu:  
    1. Book Operations
    2. User Operations
    3. Author Operations
    4. Genre Operations
    5. Quit

    """)                   
            action = input("What would you like to do? ")
            if action == "1":
                book_operations(library)
            elif action == "2":
                user_operations(library)
            elif action == "3":
                author_operations(library)
            elif action == "4":
                genre_operations(library)
            elif action == "5":
                 break
            else:
                 print("Please enter a valid response!")

if __name__ == "__main__":

    library_management_system()
                        






