# MLflow Tracker
from typing import Any, List, Dict
from mlflow.tracking import MlflowClient


class Tracker():
    def __init__(self, experiment: str, tracking_uri: str):
        self.experiment_name = experiment
        self.experiment_id = None
        self.run_id = None
        self.client = MlflowClient(tracking_uri=tracking_uri)

    def log_param(self, key: str, value: Any):
        self.client.log_param(self.run_id, key, value)

    def log_params(self, params: Dict):
        for k, v in params.items():
            self.log_param(k, v)

    def log_artifacts(self, artifacts: List[str]):
        for artifact in artifacts:
            self.client.log_artifact(self.run_id, artifact)

    def log_metrics(self, metrics: Dict[str, Any]):
        for k, v in metrics.items():
            if isinstance(v, list):
                for i in range(len(v)):
                    self.client.log_metric(self.run_id, k, v[i], step=i)
            else:
                self.client.log_metric(self.run_id, k, v)

    def start_run(self):
        try:
            self.experiment_id = self.client.create_experiment(self.experiment_name)
        except Exception:
            self.experiment_id = self.client.get_experiment_by_name(self.experiment_name).experiment_id
        run = self.client.create_run(self.experiment_id)
        self.run_id = run.info.run_id

    def end_run(self):
        self.client.set_terminated(self.run_id)
