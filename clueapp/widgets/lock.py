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

    def watch_invalid_password_entered(self, is_invalid: bool) -> None:
        self.query_exactly_one(txw.Input).set_class(is_invalid, "error")

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
