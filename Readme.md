# Getting  Started

1. Create runner class and runner parameter class. Runner class must have parameter given initializer and run method. Runner parameter must have kwargs given initializer as dataclass. 

```python
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
```


2. Register runner class and parameter class related runner name in `container.py`.

```python
runner = {
    'test': TestRunner
}

store = {
    'test': TestRunnerParameter
}
```

3. Add runner hydra styled group parameter file have runner name in runner directory.

```yml
# @package _group_
runner: test
parameter:
  name: tarou
  age: 12
```

4. Run `main.py` with custom parameter.

```sh
python main.py runner=test runner.parameter.name=jiro
```

# Cutomise processing
## Save artifacts
Runner class has artifacts property for mlflow save. You specify runner artifacts by overriding artifacts property.

```python
@property
def artifacts(self):
    return ['txt']
```

## Save Metrics
Runner class has metrics property for mlflow save. You specify runner metrics by overriding artifacts property.

```python
@property
def metrics(self):
    return {
        'a': 1,
        'b': [1, 2]
    }
```