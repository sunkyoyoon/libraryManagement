# Makefile

.PHONY: test clean run

test:
	python -m unittest test_library_system.py

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	rm -f library.db

run:
	python main.py

install:
	pip install -r requirements.txt