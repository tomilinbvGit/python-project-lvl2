install:
	poetry install

build:
	poetry build

gendiff:
	poetry run gendiff

publish:
	poetry publish --dry-run

package-install:
	python3.9 -m pip install dist/*.whl

lint:
		poetry run flake8 gendiff
		poetry run flake8 tests

pytest:
		poetry run pytest --cov=gendiff tests/ --cov-report xml
