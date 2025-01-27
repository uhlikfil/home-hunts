import logging
import os
import pathlib

import textual as tx
import textual.app as txa
import textual.containers as txc
import textual.widgets as txw

logger = logging.getLogger(__name__)


class TextWithFile(txw.Static):
    def __init__(self, text: str, file_path: pathlib.Path | str):
        """Display a text with a button to open a file.

        :param text: The text to be displayed.
        :param exec: The executable used to open the file.
        :param file_path: Path relative to the `resources` directory.
        """
        super().__init__()
        self.text = text
        self.file_path = file_path

    def compose(self) -> txa.ComposeResult:
        with txc.HorizontalGroup():
            yield txw.Markdown(self.text)
            with txc.Right():
                yield txw.Button("Open File", "primary")

    @tx.on(txw.Button.Pressed)
    def open_file(self) -> None:
        logger.info("opening %s", self.file_path)
        os.system(f"open {self.file_path}")
