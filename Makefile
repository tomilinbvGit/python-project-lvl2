install:
	poetry install

build:
	poetry build

gendiff:
	poetry run gendiff

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl

make lint:
	poetry run flake8 gendiff

test:
	poetry run pytest tests/ --cov=gendiff --cov-report=xml