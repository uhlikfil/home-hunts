import logging
import pathlib

import textual.logging as txl

from .app import ClueApp
from .app_builder import AppBuilder


def configure_logger() -> None:
    root_logger = logging.getLogger()
    handler = txl.TextualHandler()
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.DEBUG)


def create_app(game_dir: pathlib.Path | str) -> ClueApp:
    configure_logger()

    builder = AppBuilder(game_dir)
    return builder.build()


if __name__ == "__main__":
    import sys

    game_dir = sys.argv[1]
    app = create_app(game_dir)
    app.run()
