## What it Does ##
This tool converts python source code or .py files to VS code snippets

# Usage
```
from pythonsnip.pythonsnip import PythonSnip

if __name__ == "__main__":

    example_file = "examples/example.py"
    with open(example_file, "r") as f:
        source_code = f.read()
    parser = PythonSnip(source_code)
    parser.get_snippets().to_json_snippet(filename="examples/example.json")
```
**From:**
```
from dataclasses import dataclass


@dataclass
class Person:
    """random example class"""

    name: str
    age: int
    email: str

    def years_until(self, target_age: int) -> int:
        """Returns the number of years until the person reaches the target age."""
        if target_age <= self.age:
            return 0  # No years left to reach that age
        return target_age - self.age
        return target_age - self.age
```
**To:**
```
{
  "Person": {
    "prefix": "Person",
    "body": [
      "\"@dataclass\",",
      "\"class Person:\",",
      "\"    \"\"\"random example class\"\"\"\",",
      "\"    name: str\",",
      "\"    age: int\",",
      "\"    email: str\",",
      "\"\",",
      "\"    def years_until(self, target_age: int) -> int:\",",
      "\"        \"\"\"Returns the number of years until the person reaches the target age.\"\"\"\",",
      "\"        if target_age <= self.age:\",",
      "\"            return 0\",",
      "\"        return target_age - self.age\",",
      "\"        return target_age - self.age\""
    ],
    "description": "random example class"
  }
}
```