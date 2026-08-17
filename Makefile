.PHONY: install test lint run clean

install:
	pip install -e ".[dev]"

test:
	pytest

lint:
	ruff check src tests

run:
	python -m hidms

clean:
	rm -rf build dist *.egg-info .pytest_cache .ruff_cache
	find . -type d -name __pycache__ -exec rm -rf {} +
