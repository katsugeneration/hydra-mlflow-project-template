# Katsuya Shimabukuro @ 2020
# Application Main Module
import pathlib
import hydra
from omegaconf import DictConfig
from container import module, store
from tracker import Tracker


@hydra.main(config_name='config')
def main(config: DictConfig) -> None:
    cwd = pathlib.Path(hydra.utils.get_original_cwd())
    tracker = Tracker(config.experiment, tracking_uri=str(cwd.joinpath('mlruns')))
    tracker.start_run()
    tracker.log_param('module', config.module.module)
    tracker.log_params(config.module.parameter)

    parameter = store[config.module.module](**config.module.parameter)
    runner = module[config.module.module](parameter)
    runner.run()
    tracker.log_artifacts(runner.artifacts)
    tracker.log_metrics(runner.metrics)

    tracker.end_run()


if __name__ == "__main__":
    main()
