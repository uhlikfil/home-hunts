import logging

import textual.logging as txl
import textual.widgets as txw

from .app import ClueApp
from .widgets import Clue, PasswordLock


def configure_logger() -> None:
    root_logger = logging.getLogger()
    handler = txl.TextualHandler()
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.DEBUG)


def create_app() -> ClueApp:
    configure_logger()

    return ClueApp(
        "Test",
        "XXX",
        "This is a test This is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a testThis is a test",
        Clue(
            "clue 2",
            txw.Label("CONTENTS"),
        ),
        Clue(
            "clue 1",
            txw.Label("SECRET CONTENTS"),
            PasswordLock("motherlode"),
        ),
    )
