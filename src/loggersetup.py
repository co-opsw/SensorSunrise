from loguru import logger
import sys


def logger_setup(file):
    logger.remove()
    logger.add(
        f"logs/{file}",
        colorize=True,
        format="{time:YYYY-MM-DD HH:mm} | {level: <8} | {name}:{function}:{line} - {message}",
        retention="2 days",
        compression="zip",
    )
    logger.add(sys.stderr, format="{time:HH:mm} | {level: <8} | {message}")

    return logger
