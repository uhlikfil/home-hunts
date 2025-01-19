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
        case_subtitle: str,
        description: str,
        *clues: Clue,
    ):
        super().__init__()
        self.title = case_title
        self.sub_title = case_subtitle
        self.description = description
        self.clues = clues

    BINDINGS = [
        txb.Binding("down", "focus_next", description="Focus Next", priority=True),
        txb.Binding("up", "focus_previous", description="Focus Prevous", priority=True),
    ]

    def compose(self) -> txa.ComposeResult:
        yield txw.Header(show_clock=True, icon="")
        with txc.Horizontal():
            with txc.VerticalScroll():
                with txc.Center():
                    yield txw.Label(self.description, classes="description")
                yield from self.clues
            yield Matrix(classes="sidebar")
        yield txw.Footer()

    def on_mount(self) -> None:
        self.register_theme(hacker_theme)
        self.theme = "hacker"
