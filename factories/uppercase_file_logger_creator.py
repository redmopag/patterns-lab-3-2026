from interfaces import OutputStrategy
from strategies import UppercaseFileStrategy

from .file_logger_creator import FileLoggerCreator


class UppercaseFileLoggerCreator(FileLoggerCreator):
    def create_strategy(self) -> OutputStrategy:
        return UppercaseFileStrategy(self._log_file)
