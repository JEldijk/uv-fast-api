# uv-fast-api example project

this is an example project to enw explore python libs and tools

## included

- [uv](https://docs.astral.sh/uv/)
- [ruff](https://docs.astral.sh/ruff/)
- [pyright](https://github.com/microsoft/pyright)
- [fastAPI](https://fastapi.tiangolo.com/)
    - [pydantic](https://docs.pydantic.dev/latest/)


https://www.youtube.com/watch?v=ZuQzIbRoFC4&t=873s
https://www.linkedin.com/pulse/databricks-asset-bundles-uv-python-package-project-manager-pires-1uwqf
https://github.com/doug-pires/uv_dab/blob/master/pyproject.toml

## init the project

- [install uv](https://docs.astral.sh/uv/getting-started/installation/)
- install all workspace packages via `uv sync --all-packages`


## ci

- tests: `uv run pytest`
- lint: `uv run ruff`
- typecheck `uv run pyright`

## run scripts

- `uv run apps/api-2/hello.py`
- `uv run fastapi run apps/api/src/main.py`

## create libs

- `uv init --lib libs/utils`

## create apps

- `uv init --package api`