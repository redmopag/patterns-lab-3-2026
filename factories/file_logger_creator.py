from pathlib import Path

from interfaces import OutputStrategy
from strategies import FileStrategy

from .logger_creator import LoggerCreator


class FileLoggerCreator(LoggerCreator):
    def __init__(self, log_file: str | Path) -> None:
        self._log_file = log_file

    def create_strategy(self) -> OutputStrategy:
        return FileStrategy(self._log_file)
