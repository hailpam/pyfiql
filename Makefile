
all: init test

init:
	pip install --user -r requirements.txt

test:
	python -m unittest tests

.PHONY: all init tests
