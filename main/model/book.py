class Book():
    def __init__(self, state: int, title: str) -> None:
        self.state = state
        self.title = title

    def getState(self) -> int:
        return self.state

    def setState(self, state: int) -> None:
        self.state = state

    def getTitle(self) -> str:
        return self.title

    def setTitle(self, title: str) -> None:
        self.title = title