from pathlib import Path

import pytest

from strategies import ConsoleStrategy, FileStrategy, UppercaseFileStrategy


def test_console_strategy_prints_record(capsys: pytest.CaptureFixture[str]) -> None:
    ConsoleStrategy().write("2026-01-02 03:04:05 [INFO] hello")

    assert capsys.readouterr().out == "2026-01-02 03:04:05 [INFO] hello\n"


def test_file_strategy_appends_records_creating_directories(tmp_path: Path) -> None:
    log_file = tmp_path / "logs" / "app.log"
    strategy = FileStrategy(log_file)

    strategy.write("first")
    strategy.write("second")

    assert log_file.read_text(encoding="utf-8") == "first\nsecond\n"


def test_uppercase_file_strategy_writes_record_in_upper_case(tmp_path: Path) -> None:
    log_file = tmp_path / "app.log"
    strategy = UppercaseFileStrategy(log_file)

    strategy.write("2026-01-02 03:04:05 [error] something happened")

    assert log_file.read_text(encoding="utf-8") == (
        "2026-01-02 03:04:05 [ERROR] SOMETHING HAPPENED\n"
    )
