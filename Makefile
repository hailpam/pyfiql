
all: init test

init:
	pip install -r requirements.txt

test:
	python tests/test_parser.py
	python tests/test_model.py
	python tests/test_visitor.py

run-examples:
	python examples/ast_example.py
	python examples/visitor_example.py

.PHONY: all init tests run-example
