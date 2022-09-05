install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python3 -m pytest -vv -ra --cov=hello --cov=greeting tests

debug:
	python3 -m pytest -vv --pdb --cov=hello --cov=greeting tests

one-test:
	python3 -m pytest -vv tests/test_greeting.py::test_my_name

format:
	black *.py

lint:
	pylint --disable=R,C hello.py

all: install lint test