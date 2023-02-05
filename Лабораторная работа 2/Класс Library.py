BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages:int):
        if not isinstance(id_, int):
            raise TypeError("Цифру дайте нормальную, айди должно быть целым числом:(")
        if not isinstance(name, str):
            raise TypeError("Название книги должно быть типа стринг хехе")
        if not isinstance(pages, int):
            raise TypeError("Кодичество страниц должно быть целым числом")
        if pages > 0:
            self.id_ = id_
            self.name = name
            self.pages = pages
        else:
            raise TypeError("Страницы в минус ушли, ого!")
    def __str__(self) -> str:
        return f'Книга "{self.name}"'
    def __repr__(self) -> str:
        return f"Book(id_={self.id_}, name='{self.name}', pages={self.pages})"

# TODO написать класс Library
class Library:
    def __init__(self, books=None):
        if books is None:
            books=[]
        self.books=books

    def get_next_book_id(self):
        if not self.books:
            return 1
        else:
            return self.books[-1].id_ +1

    def get_index_by_book_id(self, id_:int):
        for i, book in enumerate(self.books):
            if book.id_ == id_:
                return i
            raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
