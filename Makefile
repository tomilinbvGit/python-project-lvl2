install:
	poetry install

build:
	poetry build

gendiff:
	poetry run gendiff

make lint:
		poetry run flake8 gendiff
		poetry run flake8 tests

pytest:
		poetry run pytest --cov=gendiff tests/ --cov-report xml