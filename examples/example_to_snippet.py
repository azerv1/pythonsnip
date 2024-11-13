from pythonsnip.pythonsnip import PythonSnip

if __name__ == "__main__":

    example_file = "examples/example.py"
    with open(example_file, "r") as f:
        source_code = f.read()
    parser = PythonSnip(source_code)
    parser.get_snippets().to_json_snippet(filename="examples/example.json")
