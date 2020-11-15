# Runner Base Module

class BaseRunner:
    @property
    def artifacts(self):
        return []

    @property
    def metrics(self):
        return {}

    def run(self):
        pass
