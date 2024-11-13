import inspect

from pythonsnip.pythonsnip import PythonSnip, Snippet


def test_type():
    code = inspect.getsource(PythonSnip)
    parser = PythonSnip(code=code)
    parser.get_snippets()
    parser.to_json_snippet(filename="test3.json")


def test_snippet_functions():
    pass
