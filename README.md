# ml-python-template

## Requirement

- [Python](https://www.python.org/)
- [PDM](https://pdm.fming.dev/latest/)

## Start a New Project from Template

To set up your project based on this template run the following command:

`pdm init --cookiecutter git+ssh://git@github.com/gitlost-murali/ml-python-template.git`

After that follow the `README` of the generated project for the setup.

**Note:** There was a bug with the cookiecutter pdm integration that was resolved with the release of pdm `2.10.0`. Make sure to upgrade pdm when getting an error at project initialization.

## Dependencies

The template comes with a set of pre-installed dependencies:

- [isort](https://github.com/PyCQA/isort) for import sorting
- [black](https://github.com/psf/black) for formatting
- [ruff](https://github.com/astral-sh/ruff) for linting
- [pytest](https://github.com/pytest-dev/pytest) for testing
- [pre-commit](https://pre-commit.com/) for pre-commit hooks
- [commitizen](https://commitizen-tools.github.io/commitizen/) for commit message formatting
- [mkdocs-material](https://squidfunk.github.io/mkdocs-material/) for documentation


## Directory Structure

    ├── README.md          <- The top-level README for developers using this project.
    |
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- Documentation based on mkdocs
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── src                <- Source code for use in this project.
    │   ├── <package_name>    <- Add one or multiple packages under src
    |   │   ├── __init__.py    <- Makes <package_name> a Python package
    |   │   │
    |   │   ├── data           <- Scripts to download or generate data
    |   │   │   └── make_dataset.py
    |   │   │
    |   │   ├── models         <- Scripts to train models and then use trained models to make
    |   │   │   │                 predictions
    |   │   │   ├── predict_model.py
    |   │   │   └── train_model.py
    |   │   │
    |   │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    |   │       └── visualize.py
