from .file_strategy import FileStrategy


class UppercaseFileStrategy(FileStrategy):
    def write(self, record: str) -> None:
        # механика записи в файл не дублируется: переопределяется только текст
        super().write(record.upper())
