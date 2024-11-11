import inspect
import json

from pythonsnip.pythonsnip import CodeParser, Snippet


def test_type():
    code = inspect.getsource(CodeParser)
    parser = CodeParser(code=code)
    parser.function_snippets()
    parser.class_snippets()
    parser.to_json_snippet(filename="test3.json")


def test_snippet_functions():
    import ast

    ast_file = ast.__file__
    parser = CodeParser(file=ast_file)

    functions = parser.function_snippets()
    classes = parser.class_snippets()

    for dict_snippet in parser.snippets:
        snippet = Snippet(**dict_snippet)

        original_body = snippet.body
        transformed_body = snippet._json_to_code(snippet._code_to_json())

        print(f"Original body:\n{original_body[:200]}")
        print(f"Transformed body:\n{transformed_body[:200]}")
