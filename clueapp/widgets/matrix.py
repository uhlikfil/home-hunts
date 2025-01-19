import logging
import random
import string

import rich.text
import textual.app as txa
import textual.reactive as txr
import textual.timer
import textual.widget
import textual.widgets as txw

logger = logging.getLogger(__name__)


CHARS = string.ascii_letters + string.digits + string.punctuation + " "


class Matrix(textual.widget.Widget):
    """A widget rolling random text in a Matrix style."""

    rolling: textual.timer.Timer
    matrix = txr.reactive("")

    def __init__(
        self,
        *,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
    ):
        super().__init__(
            name=name,
            id=id,
            classes=classes,
            disabled=True,
        )
        self.content = txw.Static()
        self.lines: list[str] = []

    def compose(self) -> txa.ComposeResult:
        yield self.content

    def on_mount(self) -> None:
        self.rolling = self.set_interval(0.8, self.roll_down)

    def on_resize(self) -> None:
        """Reset the matrix to current size."""
        self.rolling.pause()
        self.lines = [self.get_line() for _ in range(self.size.height)]
        self.compile_matrix()
        self.rolling.resume()

    def roll_down(self) -> None:
        self.lines.insert(0, self.get_line())
        self.lines.pop()
        self.compile_matrix()

    def roll_up(self) -> None:
        self.lines.append(self.get_line())
        self.lines.pop(0)
        self.compile_matrix()

    def compile_matrix(self) -> None:
        self.matrix = "\n".join(self.lines)

    def watch_matrix(self, new_matrix: str) -> None:
        matrix_text = rich.text.Text(new_matrix)
        self.content.update(matrix_text)

    def get_line(self) -> str:
        line_chars = random.choices(CHARS, k=self.size.width)
        return "".join(line_chars)
