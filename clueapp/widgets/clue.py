import logging

import textual.app as txa
import textual.widget
import textual.widgets as txw

from .lock import Lock, UnlockedLock

logger = logging.getLogger(__name__)


class Clue(txw.Static):
    def __init__(
        self,
        clue_name: str,
        clue_contents: textual.widget.Widget,
        clue_lock: Lock = UnlockedLock(),
    ):
        super().__init__()
        self.clue_name = clue_name
        self.clue_contents = clue_contents
        self.clue_lock = clue_lock

    def compose(self) -> txa.ComposeResult:
        with txw.Collapsible(title=self.clue_name):
            yield self.clue_lock
            yield self.clue_contents

    def on_mount(self) -> None:
        def handle_lock_change(is_locked: bool) -> None:
            self.clue_lock.set_class(not is_locked, "hidden")
            self.clue_contents.set_class(is_locked, "hidden")

        self.watch(self.clue_lock, "is_locked", handle_lock_change, init=True)
