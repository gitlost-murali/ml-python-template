# {{cookiecutter.project_name}}

## Setup

To setup the project and install the dependencies run:

`pdm install`

This will also create a git repository with a main branch and an initial commit.
Additionally it will install the pre-commit hooks.

## Development

To sort your code run:

`pdm run isort`

To format your code run:

`pdm run format`

To test your code run:

`pdm run test`

To lint your code run:

`pdm run lint`

To perform all kind of checks all at once run:

`pdm run checks`

If you want to automatically fix issues discovered with `checks` you can run:

`pdm run fix`

## Documentation

This project uses [mkdocs-material](https://squidfunk.github.io/mkdocs-material/) for documentation.
To serve the documentation with a local webserver run:

`pdm run docs:serve`

You can also build the documentation with:

`pdm run docs:build`

To content of the documentation can be find in the `docs` dir.

## CI

For automatic checks after pushing to GitHub the workflow under `.github/workflows/checks.yaml` is available. At least one pytest in the `tests/` directory is required to successfully pass the workflow.


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

