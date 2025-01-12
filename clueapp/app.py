import textual.app as txa
import textual.binding as txb
import textual.widgets as txw

from .utils import logger
from .widgets import Clue, PasswordLock


class ClueApp(txa.App[int]):
    BINDINGS = [
        txb.Binding("down", "focus_next", description="Focus Next"),
        txb.Binding("up", "focus_previous", description="Focus Prevous"),
    ]

    def compose(self) -> txa.ComposeResult:
        yield txw.Header(show_clock=True, icon="")
        yield Clue(
            "clue 2",
            txw.Label("CONTENTS"),
        )

        yield Clue(
            "clue 1",
            txw.Label("SECRET CONTENTS"),
            PasswordLock("asdf"),
        )
        yield logger
        yield txw.Footer()


if __name__ == "__main__":
    app = ClueApp()
    app.title = "Test Name"
    app.sub_title = "Test"
    app.run()
