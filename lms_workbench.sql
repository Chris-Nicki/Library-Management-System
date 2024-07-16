CREATE DATABASE LMS;

USE LMS;  
CREATE TABLE authors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(500) NOT NULL,
    birthday VARCHAR(10),
    birth_country VARCHAR(500),
    biography TEXT
);
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    library_id VARCHAR(50) NOT NULL UNIQUE,
	name VARCHAR(255) NOT NULL,
	address VARCHAR(100),
    birthday VARCHAR(10)
);
CREATE TABLE genres (
	id INT AUTO_INCREMENT PRIMARY KEY,   
    genre_name VARCHAR(200),
    genre_details VARCHAR(500)	
);
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
	isbn VARCHAR(20) NOT NULL,
    title VARCHAR(500) NOT NULL,
    author VARCHAR(500),
    genre VARCHAR(500),
	publication_Date VARCHAR(10),
    availability BOOLEAN DEFAULT 1,
    fiction VARCHAR(100) NOT NULL
   
	);

CREATE TABLE borrowed_books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    book_id INT,
    borrow_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);

SELECT * FROM authors;
SELECT * FROM genres;
SELECT * FROM books;
SELECT * FROM users;