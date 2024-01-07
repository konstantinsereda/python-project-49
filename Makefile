install:
	poetry install

brain-games:
	poetry run brain-games


brain-even:
	poetry run brain-even


brain-calc:
	poetry run brain-calc


brain-gcd:
	poetry run brain-gcd


brain-progression:
	poetry run brain_progression.py

brain-prime:
	poetry run brain_prime.py

lint:
	poetry run flake8 brain_games


build:
	rm -f dist/*
	poetry version --next-phase 0.1.6
	poetry build


publish:
	poetry publish --dry-run


package-install:
	python3 -m pip install --user dist/*.whl

