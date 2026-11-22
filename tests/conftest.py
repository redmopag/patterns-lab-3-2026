import pytest

from interfaces import OutputStrategy


class RecordingStrategy(OutputStrategy):
    def __init__(self) -> None:
        self.records: list[str] = []

    def write(self, record: str) -> None:
        self.records.append(record)


@pytest.fixture
def recording_strategy() -> RecordingStrategy:
    return RecordingStrategy()
