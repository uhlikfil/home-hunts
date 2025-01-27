import pydantic


class ClueDefinition(pydantic.BaseModel):
    name: str
    contents: str
    file_path: str | None = None
    password: str | None = None


class GameDefinition(pydantic.BaseModel):
    title: str
    subtitle: str
    description: str | None = None
    clues: list[ClueDefinition]
