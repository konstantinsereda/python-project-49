install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

lint:
	poetry run flake8 brain_games
build:
	rm -f dist/*
	poetry version --next-phase 0.1.3
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl


