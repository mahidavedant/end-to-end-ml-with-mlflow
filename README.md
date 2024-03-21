# end-to-end-ml-with-mlflow
> The dataset is related to red wine samples, from the north of Portugal. The goal is to model wine quality based on physicochemical tests. 
> * Original Source: https://archive.ics.uci.edu/dataset/186/wine+quality
>

- I've built a top-tier wine quality prediction app using `ElasticNet`, meticulously tracked with **MLflow** and **Dagshub**. 

## Workflows
1. Update `config.yaml`
2. Update `schema.yaml`
3. Update `params.yaml`
4. Update `entity`
5. Update configuration manager in src config
6. Update the `components`
7. Update the `pipeline`
8. Update `main.py`
9. Update `app.py`

---
## How to run?
---

### STEPS:

Clone the repository

```bash
https://github.com/mahidavedant/end-to-end-ml-with-mlflow
```

**STEP 01:** Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```

**STEP 02:** Install the requirements

```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

Now,

```bash
open up your local host and port
```

## MLflow

---

[Documentation](https://mlflow.org/docs/latest/index.html)

##### cmd

- mlflow ui

---
## dagshub

[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/mahidavedant/end-to-end-ml-with-mlflow.mlflow \
MLFLOW_TRACKING_USERNAME=mahidavedant \
MLFLOW_TRACKING_PASSWORD=19390786719f78c7b137e4079a8efcd41c8e84ac \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/mahidavedant/end-to-end-ml-with-mlflow.mlflow

export MLFLOW_TRACKING_USERNAME=mahidavedant

export MLFLOW_TRACKING_PASSWORD=19390786719f78c7b137e4079a8efcd41c8e84ac

```
