FROM nvidia/cuda:11.0-runtime-ubuntu20.04

RUN apt-get update
RUN apt-get install -y python3.8 python3-pip build-essential libssl-dev libffi-dev python3.8-dev
RUN pip3 install torch===1.7.0+cu110 -f https://download.pytorch.org/whl/torch_stable.html
RUN pip3 install pandas scikit-learn matplotlib seaborn mlflow hydra-core dask[dataframe] dask-ml tqdm
RUN pip3 install pytorch-lightning