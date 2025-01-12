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
    show_invalid_pwd_msg = txr.reactive(False)

    def __init__(self, password: str):
        super().__init__()
        self.password = password

    def compose(self) -> txa.ComposeResult:
        yield txw.Input(placeholder="enter password", password=True)

    def watch_show_invalid_pwd_msg(self, show: bool) -> None:
        logger.info(f"show invalid password message {show=}")
        if show:
            self.mount(txw.Label("Invalid password", id="invalid-pwd-msg"))
        else:
            self.query("#invalid-pwd-msg").remove()

    @tx.on(txw.Input.Submitted)
    def enter_password(self, event: txw.Input.Submitted) -> None:
        if event.value == self.password:
            logger.info("correct password entered")
            self.is_locked = False
            self.show_invalid_pwd_msg = False
        else:
            logger.info("invalid password entered")
            self.show_invalid_pwd_msg = True
        event.input.value = ""
