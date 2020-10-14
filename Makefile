
init:
	pip install -r requriments.txt

test:
	py.test tests

.PHONY init tests
