from interfaces import OutputStrategy


class ConsoleStrategy(OutputStrategy):
    def write(self, record: str) -> None:
        print(record)
