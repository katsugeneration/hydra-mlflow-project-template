# Test Runner module
from dataclasses import dataclass
from runner.base_runner import BaseRunner


@dataclass
class TestRunnerParameter:
    name: str
    age: int


class TestRunner(BaseRunner):
    def __init__(self, parameter: TestRunnerParameter):
        self.name = parameter.name
        self.age = parameter.age

    def run(self):
        print('%s is %d years old.' % (self.name, self.age))
