import json


def load_data_from_file(file_name):
    with open(f"data/{file_name}") as data_file:
        json_data = data_file.read()

    if not json_data:
        json_data = "[]"

    return json.loads(json_data)


""" ----- ----- ----- Books ----- ----- ----- """


def read_books_file():
    return load_data_from_file("books.json")


def get_all_book():
    return read_books_file()


def get_book(book_id):
    books_data = read_books_file()
    for book in books_data:
        if book["id"] == book_id:
            return book
