class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages
        super().__init__(name, author)

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages < 0:
            raise ValueError("Количество страниц не может быть отрицательным числом")

    def __str__(self):
        return f"{super().__str__()}. Количество страниц: {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        self.name = name
        self.author = author
        self.duration = duration
        super().__init__(name, author)

        if not isinstance(duration, float):
            raise TypeError("Продолжительность должна быть типа int")
        if duration < 0:
            raise ValueError("Продолжительность не может быть отрицательным числом")

    def __str__(self):
        return f"{super().__str__()}. Продолжительность: {self.duration}"


    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"
