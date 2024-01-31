# evidences-exercise

Interactive assignment on roles of citiens

The task is described in [here](Role%20Question.pdf).

* Summary of set up

1. brew install pipx pre-commit
2. pipx install poetry
3. cd `project`
4. poetry env use python3.12 (or path to python 3.12)
5. poetry install
6. pre-commit install
7. pre-commit install-hooks

##### Configuration #####

* All projects configuration is stored in [pyproject.toml](pyproject.toml)
* Dependencies:

```shell
* poetry add {package} ...
```

##### Testing #####
```shell
* poetry run pytest
```
