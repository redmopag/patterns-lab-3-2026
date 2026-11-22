from abc import ABC, abstractmethod

from interfaces import OutputStrategy
from logger import Logger


class LoggerCreator(ABC):
    """create_strategy — фабричный метод, переопределяется подклассами;
    create_logger — клиентская операция, написана один раз против абстракции
    и не знает, какая конкретная стратегия будет создана."""

    def create_logger(self) -> Logger:
        return Logger(self.create_strategy())

    @abstractmethod
    def create_strategy(self) -> OutputStrategy:
        raise NotImplementedError
