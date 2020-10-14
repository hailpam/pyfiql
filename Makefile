
all: init test

init:
	pip install -r requirements.txt

test:
	python -m unittest tests

.PHONY: all init tests
