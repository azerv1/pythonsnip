import ast
import json
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Snippet:
    name: str
    prefix: str
    body: str
    description: str

    def _code_to_json(self) -> dict:
        _body = self.body.split("\n")
        _len = len(_body)

        self._new_body = [
            f'"{line}",' if index < _len - 1 else f'"{line}"'
            for index, line in enumerate(_body)
        ]

        _snippet = {
            self.name: {
                "prefix": self.prefix,
                "body": self._new_body,
                "description": self.description,
            }
        }
        self._snippet = _snippet
        return _snippet


class PythonSnip:
    """Parse Python code to extract function and class definitions."""

    def __init__(self, code: str) -> None:
        self.code = code
        self.node = ast.parse(self.code)
        self.snippets: list[dict] = []

    def get_snippets(self, functions: bool = True, classes: bool = True):
        # We will gather all function and class definitions

        definitions: list[ast.FunctionDef | ast.ClassDef] = []
        if functions:
            definitions.extend(
                [node for node in self.node.body if isinstance(node, ast.FunctionDef)]
            )

        if classes:
            definitions.extend(
                [node for node in self.node.body if isinstance(node, ast.ClassDef)]
            )

        # Extract snippets from the collected definitions
        for _def in definitions:
            source = ast.unparse(_def)  # Get the source code of the function/class
            name = _def.name  # Get the name of the function/class
            docstring = ast.get_docstring(_def)  # Get the docstring

            self.snippets.append(
                {"name": name, "prefix": name, "body": source, "description": docstring}
            )

        return self

    def to_json_snippet(self, filename: Path, indent=2):
        if self.snippets:
            with open(filename, "w+") as _json_file:
                json_data = {}
                for dict_snippet in self.snippets:
                    snippet = Snippet(**dict_snippet)
                    json_snippet = snippet._code_to_json()
                    json_data.update(
                        json_snippet
                    )  # Merge the individual snippet into the main dictionary

                json.dump(json_data, _json_file, indent=indent)
        else:
            raise ValueError
