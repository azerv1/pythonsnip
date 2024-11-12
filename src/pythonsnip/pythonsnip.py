import ast
import json
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Snippet:
    name: str
    prefix: str
    body: str
    description: str | None

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

    def _json_to_code(self, data: dict) -> str:
        """This should return the starting self.body code"""
        return "\n".join(
            [
                (
                    line.strip('""').rstrip(',"')
                    if not line.endswith('""",')
                    else line[1:-2]
                )
                for line in data[self.name]["body"]
            ]
        )


@dataclass
class CodeParser:
    """Parse Python code to extract function and class definitions."""

    def __init__(self, file: Path | None = None, code: str | None = None) -> None:
        if not code and Path(file).exists():
            with open(file) as f:
                self.code = f.read()
        elif code:
            self.code = code
        self.node = ast.parse(self.code)
        self.snippets: list[dict] = []

    def class_snippets(self):
        defs = list(filter(lambda node: isinstance(node, ast.ClassDef), self.node.body))
        for _def in defs:
            source = ast.unparse(_def)
            name = _def.name
            docstring = ast.get_docstring(_def)
            self.snippets.append(
                {"name": name, "prefix": name, "body": source, "description": docstring}
            )
        return self.snippets

    def function_snippets(self):
        defs = list(
            filter(lambda node: isinstance(node, ast.FunctionDef), self.node.body)
        )

        for _def in defs:
            source = ast.unparse(_def)
            name = _def.name
            docstring = ast.get_docstring(_def)

            self.snippets.append(
                {"name": name, "prefix": name, "body": source, "description": docstring}
            )
            return self.snippets

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
            return False
