from db.run_sql import run_sql
from models.book import Book
from repositories.author_repository import author_repository


def save(book):
    sql = 'INSERT INTO books (first_name, last_name) VALUES (%s, %s) RETURNING *'
    values = [book.first_name, book.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def select_all():
    books = []

    sql = 'SELECT * FROM authors'
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(row['title'], row['genre'], row['publisher'], author, row['id'])
        books.append(book)
    return books

def select(id):
    author = None
    sql = 'SELECT * FROM authors WHERE id=%s'
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = Author(result['first_name'], result['last_name'], result['id'])
    return author

def delete_all():
    sql = 'DELETE FROM authors'
    run_sql(sql)

def delete(id):
    sql = 'DELETE FROM authors WHERE id=%s'
    values = [id]
    run_sql(sql, values)