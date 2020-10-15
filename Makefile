
all: init test

init:
	pip install -r requirements.txt

test:
	python tests/test_parser.py
	python tests/test_model.py

.PHONY: all init tests
