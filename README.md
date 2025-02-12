# uv-fast-api example project

this is an example project to explore python libs and tools relevant for data-engineering.

## included tech

- [uv](https://docs.astral.sh/uv/)
- [ruff](https://docs.astral.sh/ruff/)
- [pyright](https://github.com/microsoft/pyright)
- [fastAPI](https://fastapi.tiangolo.com/)
    - [pydantic](https://docs.pydantic.dev/latest/)
- [bundles](https://docs.databricks.com/en/dev-tools/bundles/index.html)
    - [setting-secrets](https://docs.databricks.com/en/security/secrets/secrets-spark-conf-env-var.html#reference-a-secret-with-a-spark-configuration-property)
- IDE setup
    - [sqltools](https://docs.databricks.com/en/dev-tools/sqltools-driver.html)
    - [bundles-extension](https://docs.databricks.com/en/dev-tools/vscode-ext/index.html)

## inspiration

- [video on monorepo asset bundles setup](https://www.youtube.com/watch?v=ZuQzIbRoFC4&t=873s)
- [blog on how to set up bundles with uv](ttps://www.linkedin.com/pulse/databricks-asset-bundles-uv-python-package-project-manager-pires-1uwqf)
    - [example repo from blog](https://github.com/doug-pires/uv_dab/blob/master/pyproject.toml)

## init the project

- [install uv](https://docs.astral.sh/uv/getting-started/installation/)
- install all workspace packages via `uv sync --all-packages`


## ci

- tests: `uv run pytest`
- lint: `uv run ruff`
- typecheck `uv run pyright`

## run app scripts

- `uv run apps/api-2/hello.py`
- `uv run fastapi run apps/api/src/main.py`

## create libs

- `uv init --lib libs/utils`

## create apps

- `uv init --package api`

## create bundle

- `cd bundles`
- `databricks bundle init default-python`
- follow instructions and set a name <exampel-name>
- `uv init . --lib`
- remove the files, they are replaced by the project.toml:
    - setup.py
    - requirements-dev.txt
    - pytest.ini
- in newly created databricks.yml' add:
   ```yml
   artifacts:
    default:
        type: whl
        build: uv build --wheel
        path: .  
   ```