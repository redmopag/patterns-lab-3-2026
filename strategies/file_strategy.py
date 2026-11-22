from pathlib import Path

from interfaces import OutputStrategy


class FileStrategy(OutputStrategy):
    def __init__(self, log_file: str | Path) -> None:
        self._log_file = Path(log_file)

    def write(self, record: str) -> None:
        self._log_file.parent.mkdir(parents=True, exist_ok=True)
        with self._log_file.open("a", encoding="utf-8") as stream:
            stream.write(record + "\n")
