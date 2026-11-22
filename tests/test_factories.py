import pytest

from factories import (
    ConsoleLoggerCreator,
    FileLoggerCreator,
    LoggerCreator,
    UppercaseFileLoggerCreator,
)
from interfaces import OutputStrategy
from strategies import ConsoleStrategy, FileStrategy, UppercaseFileStrategy


@pytest.mark.parametrize(
    "creator, strategy_type",
    [
        (ConsoleLoggerCreator(), ConsoleStrategy),
        (FileLoggerCreator("app.log"), FileStrategy),
        (UppercaseFileLoggerCreator("app.log"), UppercaseFileStrategy),
    ],
)
def test_create_strategy_returns_concrete_strategy(
    creator: LoggerCreator, strategy_type: type[OutputStrategy]
) -> None:
    assert isinstance(creator.create_strategy(), strategy_type)
