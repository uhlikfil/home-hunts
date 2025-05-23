import pathlib

import textual.app as txa
import textual.binding as txb
import textual.containers as txc
import textual.widgets as txw

from .theme import hacker_theme
from .widgets import Clue, Matrix


class ClueApp(txa.App[int]):
    CSS_PATH = pathlib.Path(__file__).parent / "resources/styles.tcss"

    def __init__(
        self,
        case_title: str,
        case_subtitle: str | None,
        case_description: str | None,
        *clues: Clue,
    ):
        super().__init__()
        self.title = case_title
        self.sub_title = case_subtitle if case_subtitle else ""
        self.description = (
            txc.Center(txw.Label(case_description, classes="description"))
            if case_description
            else txw.Static(classes="hidden")
        )
        self.clues = clues

    BINDINGS = [
        txb.Binding("down", "focus_next", description="Focus Next", priority=True),
        txb.Binding("up", "focus_previous", description="Focus Prevous", priority=True),
    ]

    def compose(self) -> txa.ComposeResult:
        yield txw.Header(show_clock=True, icon="")
        with txc.HorizontalGroup():
            with txc.VerticalScroll():
                yield self.description
                yield from self.clues
            yield Matrix(classes="sidebar")
        yield txw.Footer()

    def on_mount(self) -> None:
        self.register_theme(hacker_theme)
        self.theme = "hacker"
