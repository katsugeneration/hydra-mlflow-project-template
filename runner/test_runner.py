# Test Runner module
from dataclasses import dataclass


@dataclass
class TestRunnerParameter:
    name: str
    age: int


class TestRunner():
    def __init__(self, parameter: TestRunnerParameter):
        self.name = parameter.name
        self.age = parameter.age

    def run(self):
        print('%s is %d years old.' % (self.name, self.age))
