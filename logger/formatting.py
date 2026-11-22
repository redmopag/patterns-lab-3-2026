from datetime import datetime

from .levels import LogLevel

TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"


def format_record(level: LogLevel, message: str, now: datetime | None = None) -> str:
    """Собирает запись вида `YYYY-MM-DD HH:mm:ss [LEVEL] Message`."""
    # now необязателен: тесты передают фиксированное время ради детерминизма
    timestamp = (now or datetime.now()).strftime(TIMESTAMP_FORMAT)
    return f"{timestamp} [{level.value}] {message}"
