from . import Book
from main.subject import AlarmBook

class Library():

    def __init__(self, alarmBook: AlarmBook) -> None:
        self.alarmBook = alarmBook

    def returnsBook(self, book: Book) -> None:
        if book.getState() == 0:
            self.alarmBook.notify_observer()