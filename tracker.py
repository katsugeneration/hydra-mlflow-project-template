# MLflow Tracker
from typing import Any
from mlflow.tracking import MlflowClient


class Tracker():
    def __init__(self, experiment: str, tracking_uri: str):
        self.experiment_name = experiment
        self.experiment_id = None
        self.run_id = None
        self.client = MlflowClient(tracking_uri=tracking_uri)

    def log_param(self, key: str, value: Any):
        self.client.log_param(self.run_id, key, value)

    def log_params(self, params: dict):
        for k, v in params.items():
            self.log_param(k, v)

    def start_run(self):
        try:
            self.experiment_id = self.client.create_experiment(self.experiment_name)
        except Exception:
            self.experiment_id = self.client.get_experiment_by_name(self.experiment_name).experiment_id
        run = self.client.create_run(self.experiment_id)
        self.run_id = run.info.run_id

    def end_run(self):
        self.client.set_terminated(self.run_id)
