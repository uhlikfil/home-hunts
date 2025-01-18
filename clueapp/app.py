import pathlib

import textual.app as txa
import textual.binding as txb
import textual.widgets as txw

from clueapp.widgets import Clue


class ClueApp(txa.App[int]):
    CSS_PATH = pathlib.Path(__file__).parent / "styles.tcss"

    def __init__(
        self,
        case_title: str,
        case_subtitle: str,
        *clues: Clue,
    ) -> None:
        super().__init__()
        self.title = case_title
        self.sub_title = case_subtitle
        self.clues = clues

    BINDINGS = [
        txb.Binding("down", "focus_next", description="Focus Next"),
        txb.Binding("up", "focus_previous", description="Focus Prevous"),
    ]

    def compose(self) -> txa.ComposeResult:
        yield txw.Header(show_clock=True, icon="")
        yield from self.clues
        yield txw.Footer()
