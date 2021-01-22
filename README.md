# Cool chip

## Getting started

### Requirements

- Conda
- Docker and Docker compose (Optional)

### Create conda environment

```bash
conda env create -f environment.yml
conda activate cool
```

### Install jupyter lab extension

```bash
jupyter-labextension install --no-build $(cat labextensions.txt)
jupyter lab build --dev-build=False --minimize=False
```

### Install package in dev mode

```bash
pip install -e .
```
