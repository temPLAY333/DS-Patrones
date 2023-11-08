from main.model import Book
from main.model import Library
from main.subject import AlarmBook
from main.observer import Administration
from main.observer import Stock
from main.observer import Shopping


class Cliente():

    def run(self):
        alarm = AlarmBook()
        alarm.attach(Administration())
        alarm.attach(Stock())
        alarm.attach(Shopping())
        book = Book(1, "Economia en una Leccion")
        book.setState(0)
        library = Library(alarm)
        library.returnsBook(book)