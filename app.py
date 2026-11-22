from factories import ConsoleLoggerCreator, FileLoggerCreator, UppercaseFileLoggerCreator
from logger import LogLevel


def main() -> None:
    console = ConsoleLoggerCreator().create_logger()
    console.log(LogLevel.INFO, "Application started")

    file_logger = FileLoggerCreator("logs/app.log").create_logger()
    file_logger.log(LogLevel.WARN, "Low disk space")

    upper_file = UppercaseFileLoggerCreator("logs/app.log").create_logger()
    upper_file.log(LogLevel.ERROR, "Example error")

    try:
        console.log("DEBUG", "Wrong level example")
    except ValueError as error:
        print(f"ValueError: {error}")


if __name__ == "__main__":
    main()
