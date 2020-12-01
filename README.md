# JSON Tool

Simple tool to bulk add a property to all .json files in a directory structure.

## Development Environment

- pyenv for python versioning
- pipenv for virtual environment
- setup taken from this guide <https://hackernoon.com/reaching-python-development-nirvana-bb5692adf30c>, as well as https://dev.to/py3course/setting-up-a-python-environment-in-2020-3e9e

### Get started

- clone the repo
- ensure you have pipenv installed
- run `pipenv shell` to get a shell in a virtual environment
- run the app with `pipenv run python app.py --help`
- to add `{"foo":"bar"}` to input json, run with `pipenv run python app.py --key foo --value bar`

## Ackowledgements

Fake data courtesy: <https://jsonplaceholder.typicode.com/>

Setup from: <https://hackernoon.com/reaching-python-development-nirvana-bb5692adf30c>

and https://dev.to/py3course/setting-up-a-python-environment-in-2020-3e9e

Gitignore: <https://github.com/github/gitignore/blob/master/Python.gitignore>

Tests influenced by: <https://semaphoreci.com/community/tutorials/testing-python-aapplications-with-pytest>

## Todo

<https://tryexceptpass.org/article/pytest-github-integration/>
