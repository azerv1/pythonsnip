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
