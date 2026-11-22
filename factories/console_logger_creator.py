from interfaces import OutputStrategy
from strategies import ConsoleStrategy

from .logger_creator import LoggerCreator


class ConsoleLoggerCreator(LoggerCreator):
    def create_strategy(self) -> OutputStrategy:
        return ConsoleStrategy()
