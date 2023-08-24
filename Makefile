
install:
	poetry install

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

test-coverage:
	poetry run pytest --cov=gendiff  --cov-report xml

test:
	poetry run pytest tests/

selfcheck:
	poetry check

check: selfcheck lint #test

build: check
	poetry build
