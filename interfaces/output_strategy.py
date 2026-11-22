from abc import ABC, abstractmethod


class OutputStrategy(ABC):
    @abstractmethod
    def write(self, record: str) -> None:
        """Записывает готовую отформатированную запись в целевой приёмник."""
        raise NotImplementedError
