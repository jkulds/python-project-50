
install:
	poetry install

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

test-coverage:
	pytest --cov=gendiff

test:
	poetry run pytest

selfcheck:
	poetry check

check: selfcheck lint #test

build: check
	poetry build
