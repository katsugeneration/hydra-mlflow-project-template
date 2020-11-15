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

    @property
    def artifacts(self):
        return ['txt']

    @property
    def metrics(self):
        return {
            'a': 1,
            'b': [1, 2]
        }

    def run(self):
        print('%s is %d years old.' % (self.name, self.age))
        with open('txt', 'w') as f:
            f.write('%s is %d years old.' % (self.name, self.age))
