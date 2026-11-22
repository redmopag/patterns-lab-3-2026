from interfaces import OutputStrategy

from .formatting import format_record
from .levels import LogLevel

_VALID_LEVELS = frozenset(item.value for item in LogLevel)


class Logger:
    """Контекст Strategy: формирует запись и передаёт её стратегии вывода."""

    def __init__(self, strategy: OutputStrategy) -> None:
        self._strategy = strategy

    def log(self, level: LogLevel | str, message: str) -> str:
        # нормализация на границе в стиле Logger.setLevel из stdlib: всё, что
        # не enum, проверяется по допустимым значениям и приводится к enum;
        # проверка через not isinstance(LogLevel) важна, потому что LogLevel —
        # str-Enum и его члены сами являются строками
        if not isinstance(level, LogLevel):
            if level not in _VALID_LEVELS:
                valid = ", ".join(sorted(_VALID_LEVELS))
                raise ValueError(f"Неизвестный уровень {level!r}; допустимые: {valid}")
            level = LogLevel(level)
        record = format_record(level, message)
        self._strategy.write(record)
        return record
