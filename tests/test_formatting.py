from datetime import datetime

import pytest

from logger import LogLevel, format_record


@pytest.mark.parametrize("level", list(LogLevel))
def test_format_record_builds_exact_line(level: LogLevel) -> None:
    record = format_record(level, "hello", datetime(2026, 1, 2, 3, 4, 5))

    assert record == f"2026-01-02 03:04:05 [{level.value}] hello"


def test_format_record_uses_current_time_by_default() -> None:
    expected_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    record = format_record(LogLevel.INFO, "hello")

    assert record == f"{expected_time} [INFO] hello"
