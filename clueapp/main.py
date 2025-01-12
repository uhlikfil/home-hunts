import logging

import textual.logging as txl
import textual.widgets as txw

from clueapp.app import ClueApp
from clueapp.widgets import Clue, PasswordLock


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
