import pytest

from logger import LogLevel, Logger


def test_log_returns_record_and_passes_it_to_strategy(recording_strategy) -> None:
    record = Logger(recording_strategy).log(LogLevel.INFO, "hello")

    assert recording_strategy.records == [record]
    assert "[INFO] hello" in record


def test_log_accepts_level_as_string(recording_strategy) -> None:
    record = Logger(recording_strategy).log("WARN", "careful")

    assert "[WARN] careful" in record


@pytest.mark.parametrize("level", ["DEBUG", "info", "", 42, None])
def test_log_rejects_unknown_level(recording_strategy, level: object) -> None:
    logger = Logger(recording_strategy)

    with pytest.raises(ValueError):
        logger.log(level, "hello")

    assert recording_strategy.records == []
