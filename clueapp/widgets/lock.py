import textual.app as txa
import textual.reactive as txr
import textual.widgets as txw


class Lock(txw.Static):
    is_locked = txr.reactive(True)


class UnlockedLock(Lock):
    is_locked = txr.reactive(False)


class PasswordLock(Lock):
    def __init__(
        self,
        password: str,
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
        self.password = password

    def compose(self) -> txa.ComposeResult:
        yield txw.Input(placeholder="enter password")
