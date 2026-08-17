.PHONY: install test lint run demo train-demo web clean

install:
	pip install -e ".[dev]"

test:
	pytest

lint:
	ruff check src tests

run:
	python -m hidms

train-demo:
	python scripts/train_demo.py

demo:
	python -m hidms.demo --sample

web:
	streamlit run app.py

clean:
	rm -rf build dist *.egg-info .pytest_cache .ruff_cache
	find . -type d -name __pycache__ -exec rm -rf {} +
