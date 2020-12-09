DROP TABLE IF EXISTS authors;
DROP TABLE IF EXISTS books;

CREATE TABLE authors (
    id SERIAL PRIMARY KEY
    first_name VARCHAR(255),
    last_name VARCHAR(255),
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY  
    title VARCHAR(255)
    genre VARCHAR(255)
    publisher VARCHAR(255)
    autor_id INT REFERENCES authors(id)
);
