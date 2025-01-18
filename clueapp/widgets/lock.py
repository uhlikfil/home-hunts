import logging

import textual as tx
import textual.app as txa
import textual.reactive as txr
import textual.widgets as txw

logger = logging.getLogger(__name__)


class Lock(txw.Static):
    is_locked = txr.reactive(True)


class UnlockedLock(Lock):
    is_locked = txr.reactive(False)


class PasswordLock(Lock):
    invalid_password_entered = txr.reactive(False)

    def __init__(self, password: str):
        super().__init__()
        self.password = password

    def compose(self) -> txa.ComposeResult:
        yield txw.Input(placeholder="enter password", password=True)
        yield txw.Label("Invalid password", classes="hidden")

    def watch_invalid_password_entered(self) -> None:
        is_hidden = not self.invalid_password_entered
        self.query_exactly_one(txw.Label).set_class(is_hidden, "hidden")

    @tx.on(txw.Input.Submitted)
    def enter_password(self, event: txw.Input.Submitted) -> None:
        if event.value == self.password:
            logger.info("correct password entered")
            self.is_locked = False
            self.invalid_password_entered = False
        else:
            logger.info("invalid password entered")
            self.invalid_password_entered = True
        event.input.value = ""
