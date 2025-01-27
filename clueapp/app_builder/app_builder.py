import pathlib

import textual.widgets as txw
import yaml

from clueapp.app import ClueApp
from clueapp.widgets import Clue, PasswordLock, TextWithFile, UnlockedLock

from .definition_model import ClueDefinition, GameDefinition


class AppBuilder:
    def __init__(self, game_dir: pathlib.Path | str):
        """Create a game based on the yaml definition.

        :param game_dir: The directory name in `resources/games`.
        """
        self.game_dir = pathlib.Path(game_dir)

    def build(self) -> ClueApp:
        with open(self.game_dir / "definition.yml") as f:
            game_dict = yaml.full_load(f)
        game_def = GameDefinition.model_validate(game_dict)

        return self.to_app(game_def)

    def to_app(self, game_def: GameDefinition) -> ClueApp:
        return ClueApp(
            game_def.title,
            game_def.subtitle,
            game_def.description,
            *(self.to_clue(c) for c in game_def.clues),
        )

    def to_clue(self, clue_def: ClueDefinition) -> Clue:
        lock = PasswordLock(clue_def.password) if clue_def.password else UnlockedLock()
        contents = (
            TextWithFile(clue_def.contents, self.game_dir / clue_def.file_path)
            if clue_def.file_path
            else txw.Markdown(clue_def.contents)
        )
        return Clue(clue_def.name, contents, lock)
