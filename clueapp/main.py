import logging

import textual.logging as txl
import textual.widgets as txw

from .app import ClueApp
from .widgets import Clue, PasswordLock, TextWithFile


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
        None,
        Clue(
            "AAA asd",
            TextWithFile(
                "ASDF 7 EGIAIASDF EGIAIASDF EGIAIASDF EGIAIASDF EGIAIASDF EGIAI AIOGSIOFASDF ASDF EGIAI AIOGSIOFASDF ASDF EGIAI AIOGSIOFASDF ASDF EGIAI AIOGSIOFASDF ASDF EGIAI AIOGSIOFASDF ASDF EGIAI AIOGSIOFASDF ASDF EGIAI AIOGSIOF",
                "clueapp/resources/games/demo/road.jpg",
            ),
        ),
        Clue(
            "BBBBB hello",
            txw.Label("SECRET CONTENTS"),
            PasswordLock("motherlode"),
        ),
    )
