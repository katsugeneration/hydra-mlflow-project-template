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


2. Register runner class and parameter class related module name in `container.py`.

```python
module = {
    'test': TestRunner
}

store = {
    'test': TestRunnerParameter
}
```

3. Add module hydra styled group parameter file have module name in module directory.

```yml
# @package _group_
module: test
parameter:
  name: tarou
  age: 12
```

4. Run `main.py` with custom parameter.

```sh
python main.py module=test module.parameter.name=jiro
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