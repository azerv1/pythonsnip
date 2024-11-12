from pythonsnip.pythonsnip import CodeParser, Snippet

if __name__ == "__main__":
    example_file = "examples/example.py"
    parser = CodeParser(file=example_file)
    parser.function_snippets()
    parser.class_snippets()
    parser.to_json_snippet(filename="examples/example.json")
