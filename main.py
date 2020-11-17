# Katsuya Shimabukuro @ 2020
# Application Main Module
import pathlib
import hydra
from omegaconf import DictConfig
import container
from tracker import Tracker


@hydra.main(config_name='config')
def main(config: DictConfig) -> None:
    cwd = pathlib.Path(hydra.utils.get_original_cwd())
    tracker = Tracker(config.experiment, tracking_uri=str(cwd.joinpath('mlruns')))
    tracker.start_run()
    tracker.log_param('runner', config.runner.runner)
    tracker.log_params(config.runner.parameter)

    parameter = container.store[config.runner.runner](**config.runner.parameter)
    runner = container.runner[config.runner.runner](parameter)
    runner.run()
    tracker.log_artifacts(runner.artifacts)
    tracker.log_metrics(runner.metrics)

    tracker.end_run()


if __name__ == "__main__":
    main()
