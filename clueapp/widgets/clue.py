import textual.app as txa
import textual.widget
import textual.widgets as txw

from .lock import Lock, UnlockedLock


class Clue(txw.Static):
    def __init__(
        self,
        clue_name: str,
        clue_contents: textual.widget.Widget,
        clue_lock: Lock = UnlockedLock(),
        *,
        expand: bool = False,
        shrink: bool = False,
        markup: bool = True,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
        disabled: bool = False,
    ):
        super().__init__(
            expand=expand,
            shrink=shrink,
            markup=markup,
            name=name,
            id=id,
            classes=classes,
            disabled=disabled,
        )
        self.clue_name = clue_name
        self.clue_contents = clue_contents
        self.clue_lock = clue_lock

    def compose(self) -> txa.ComposeResult:
        with txw.Collapsible(title=self.clue_name):
            if self.clue_lock.is_locked:
                yield self.clue_lock
            else:
                yield self.clue_contents
