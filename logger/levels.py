from enum import Enum


class LogLevel(str, Enum):
    TRACE = "TRACE"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    FATAL = "FATAL"
