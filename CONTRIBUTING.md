# {{repository_name}} contributing guide

## Pipelines

CI is run using [`nox`](https://nox.thea.codes/). Before creating a PR make sure all default pipelines have passed.

### How to use nox

Nox must be downloaded with `pip install nox`.

You can run all default pipelines with just `nox` or specific ones with `nox -s foo bar`. To see all available pipelines run `nox -l`.

If you have a slow connection use `nox --no-install` to skip installing dependencies.

## Style-guide

Formatting is done by black and is checked by flake8. The project loosely follows [pep8](https://www.python.org/dev/peps/pep-0008/), but anything that is not covered by black or flake8 is up to the developer.

Refer to [pyright's type-completness guidelines](https://github.com/microsoft/pyright/blob/main/docs/typed-libraries.md) and [standard typing library's type-completness guidelines](https://github.com/python/typing/blob/master/docs/libraries.md) to see how to properly type your code.
