# Katsuya Shimabukuro @ 2020
# Application Main Module
import hydra
from omegaconf import DictConfig
from container import module, store


@hydra.main(config_name='config')
def main(config: DictConfig) -> None:
    parameter = store[config.module](**config.parameter)
    runner = module[config.module](parameter)
    runner.run()


if __name__ == "__main__":
    main()
